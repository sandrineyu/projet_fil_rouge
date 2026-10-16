"""API de prédiction.

Lancer en local : uvicorn app.main:app --reload
Documentation interactive : http://127.0.0.1:8000/docs
"""
import json
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

MODELS = Path(__file__).resolve().parent.parent / "models"
pipe = joblib.load(MODELS / "model.joblib")
meta = json.load(open(MODELS / "metadata.json"))
FEATURES = meta["features"]["numeric"] + meta["features"]["categorical"] + meta["features"]["passthrough"]

app = FastAPI(title="API fil rouge — MBA Data & BI", version="1.0")


class Observation(BaseModel):
    """Une observation à scorer : un dictionnaire {variable: valeur}."""
    features: dict[str, Any] = Field(..., examples=[{
        "age": 45, "heure": 18, "lum": 1, "atm": 1, "catr": 3, "surf": 1,
        "sexe": 1, "week_end": 0, "en_agglo": 0}])


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/model-info")
def model_info():
    return meta


@app.post("/predict")
def predict(obs: Observation):
    manquantes = [f for f in FEATURES if f not in obs.features]
    if manquantes:
        raise HTTPException(status_code=422, detail=f"Variables manquantes : {manquantes}")
    X = pd.DataFrame([{f: obs.features[f] for f in FEATURES}])
    proba = float(pipe.predict_proba(X)[0, 1])
    return {"probabilite": round(proba, 4), "seuil": meta["seuil"], "alerte": proba >= meta["seuil"],
            "modele": meta["modele"]}
