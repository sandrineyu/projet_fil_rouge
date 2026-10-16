from pathlib import Path
 
import duckdb
 
ROOT = Path(__file__).resolve().parent.parent

DATA = ROOT / "data"

BASE_CSV = ROOT / "Base.csv"

MERGED_CSV = DATA / "dataset.csv"

DB_PATH = DATA / "fraud.duckdb"
 
 
def main() -> None:

    if not BASE_CSV.exists():

        raise FileNotFoundError(f"{BASE_CSV} : télécharger Base.csv sur Kaggle et le placer à la racine du projet")
 
    DB_PATH.unlink(missing_ok=True)

    con = duckdb.connect(str(DB_PATH))
 
    # 1. Chargement de Base.csv dans la table applications

    con.execute(f"""

        CREATE TABLE applications AS

        SELECT * FROM read_csv('{BASE_CSV.as_posix()}', header = true)

    """)
 
    # 2. Export du fichier chargé

    con.execute(f"""

        COPY applications TO '{MERGED_CSV.as_posix()}' (HEADER, DELIMITER ',')

    """)
 
    # 3. Contrôles

    n_rows = con.execute("SELECT count(*) FROM applications").fetchone()[0]

    n_cols = len(con.execute("DESCRIBE applications").fetchall())

    print(f"Table applications : {n_rows:,} lignes, {n_cols} colonnes")

    print(con.sql("""

        SELECT month, count(*) AS lignes, round(avg(fraud_bool) * 100, 3) AS taux_fraude_pct

        FROM applications GROUP BY month ORDER BY month

    """))

    print(f"Base DuckDB : {DB_PATH}")

    print(f"CSV exporté : {MERGED_CSV}")

    con.close()
 
 
if __name__ == "__main__":

    main()

