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

