from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PARTS = [DATA / f"dataset_part{i}.csv" for i in (1, 2, 3)]
MERGED_CSV = DATA / "dataset.csv"
DB_PATH = DATA / "fraud.duckdb"


def main() -> None:
    for part in PARTS:
        if not part.exists():
            raise FileNotFoundError(part)

    DB_PATH.unlink(missing_ok=True)
    con = duckdb.connect(str(DB_PATH))

    # 1. Chargement et fusion : les 3 fichiers ont le même schéma,
    #    on les empile en gardant le nom du fichier d'origine.
    files = ", ".join(f"'{p.as_posix()}'" for p in PARTS)
    con.execute(f"""
        CREATE TABLE applications AS
        SELECT * EXCLUDE (filename), regexp_extract(filename, '[^/]+$') AS source_file
        FROM read_csv([{files}], header = true, union_by_name = true, filename = true)
    """)

    # 2. Export du fichier fusionné (sans la colonne technique source_file)
    con.execute(f"""
        COPY (SELECT * EXCLUDE (source_file) FROM applications)
        TO '{MERGED_CSV.as_posix()}' (HEADER, DELIMITER ',')
    """)

    # 3. Contrôles
    n_rows = con.execute("SELECT count(*) FROM applications").fetchone()[0]
    n_cols = len(con.execute("DESCRIBE applications").fetchall())
    print(f"Table applications : {n_rows:,} lignes, {n_cols} colonnes")
    print(con.sql("""
        SELECT source_file, count(*) AS lignes, min(month) AS mois_min, max(month) AS mois_max,
               round(avg(fraud_bool) * 100, 3) AS taux_fraude_pct
        FROM applications GROUP BY source_file ORDER BY source_file
    """))
    print(f"Base DuckDB : {DB_PATH}")
    print(f"CSV fusionné : {MERGED_CSV}")
    con.close()


if __name__ == "__main__":
    main()
