import io
import joblib
import pandas as pd
from fastapi import FastAPI,HTTPException,UploadFile,File
from fastapi.responses import StreamingResponse
from app.schemas import HouseData

app = FastAPI(
    title="House Price Prediction API",
    description="REST API for predicting California house prices using a Random Forest Regressor.",
    version="1.0.0"
)
model = joblib.load('../model/house_model.joblib')
features = joblib.load('../model/house_features.joblib')

@app.get("/")
def home():
    return {"message": "Welcome to the House Price Prediction API!",
            "status": "Active",
            "version": "1.0.0",
            "endpoints": "Send post request to /predict : POST endpoint to predict house prices based on input features"
            }

@app.get("/features")
def get_features():
    return {"features": features}

@app.get("/model-info")
def get_model_info():
    return {
            "model": "Random Forest Regressor",
            "version": "1.0",
            "dataset": "California Housing Dataset",
            "features": features,
            "target_variable": "Median House Value",
            "avg_error":"$25,602"
            }

@app.get("/health")
def health_check():
    return {"status": "Healthy",
            "version": "1.0.0",
            "model":"Random Forest Regressor",
            "features": features,
            "target_variable": "Median House Value",
            "avg_error":"$25,602"}

