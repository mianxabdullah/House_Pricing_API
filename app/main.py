import io
import joblib
import pandas as pd
from fastapi import FastAPI,HTTPException,UploadFile,File
from fastapi.responses import StreamingResponse


app = FastAPI(
    title="House Price Prediction API",
    description="REST API for predicting California house prices using a Random Forest Regressor.",
    version="1.0.0"
)
model = joblib.load('../model/house_model.joblib')
features = joblib.load('../model/house_features.joblib')

from app.schemas import HouseData

@app.get("/")
def home():
    return {"message": "Welcome to the House Price Prediction API!",
            "status": "Active",
            "version": "1.0.0",
            "endpoints": "Send post request to /predict : POST endpoint to predict house prices based on input features"
            }

