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

@app.post("/predict")
def predict_house_price(house: HouseData):

        input_data = pd.DataFrame([house.model_dump()]) # Convert the input data to a pandas DataFrame
        prediction = model.predict(input_data)
        price_usd = prediction[0] * 100000  # Convert to USD
        return {"predicted_price": f"${price_usd:,.0f}",
                "predicted_price_short": f"{prediction[0]:,.2f} hundred thousands $",
                "estimation_range":f"{price_usd - 25602:,.0f} to ${price_usd + 25602:,.0f}"}   


