# 🏠 House Price Prediction API

A RESTful API built with **FastAPI** that predicts California house prices using a trained **Random Forest Regressor**. The API supports both **single-house predictions** and **batch predictions via CSV uploads**, making it useful for individual predictions as well as bulk processing.

---

## 🚀 Features

- 🔮 Predict the price of a single house
- 📂 Batch prediction using CSV file uploads
- ✅ Automatic request validation with Pydantic
- 📥 Download prediction results as a CSV file
- 📊 Model information endpoint
- 📝 Feature information endpoint
- ❤️ Health check endpoint
- 📖 Interactive API documentation (Swagger UI & ReDoc)

---

## 🛠 Tech Stack

- Python 3.13
- FastAPI
- Pydantic
- Pandas
- Scikit-learn
- Joblib
- Uvicorn

---

## 📁 Project Structure

```
HOUSE_PRICING_API/
│
├── app/
│   ├── main.py
│
├── model/
│   ├── house_model.joblib
│   └── house_features.joblib
│
├── data/
│   ├── california_housing.csv
│   ├── test.csv
│   └── predictions.csv
│
├── training/
│   ├── train.py
│   └── explore.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/House_Pricing_API.git

cd House_Pricing_API
```

### Create a virtual environment

Windows

```powershell
python -m venv venv
```

Activate

```powershell
.\venv\Scripts\Activate.ps1
```

macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## 📖 Interactive Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API home page |
| GET | `/health` | API health status |
| GET | `/features` | List of model features |
| GET | `/model-info` | Information about the trained model |
| POST | `/predict` | Predict a single house price |
| POST | `/predict_file` | Batch prediction using a CSV file |

---

## Example Request

### POST `/predict`

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41,
  "AveRooms": 6.98,
  "AveBedrms": 1.02,
  "Population": 322,
  "AveOccup": 2.55,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

---

## Example Response

```json
{
  "predicted_price": "$452,300",
  "predicted_price_short": "$4.52 hundred thousands",
  "estimation_range": "$426,698 to $477,902"
}
```

---

## CSV Batch Prediction

Upload a CSV containing the following columns:

```
MedInc
HouseAge
AveRooms
AveBedrms
Population
AveOccup
Latitude
Longitude
```

The API returns a downloadable CSV containing an additional column:

```
PredictedPrice
```

---

## Input Validation

The API validates incoming requests using Pydantic.

Examples include:

- Median Income > 0
- House Age ≥ 0
- Latitude between 32 and 42
- Longitude between -125 and -114

Invalid requests return appropriate HTTP status codes with descriptive error messages.

---

## Machine Learning Model

- **Algorithm:** Random Forest Regressor
- **Dataset:** California Housing Dataset
- **Average Prediction Error:** ± $25,602

---

## Future Improvements

This project intentionally focuses on FastAPI fundamentals.

Possible future enhancements include:

- Docker support
- PostgreSQL integration
- Prediction history
- JWT Authentication
- Unit testing with Pytest
- Cloud deployment
- Logging and monitoring

---

## Author

**Mian Abdullah**

Data Science Student

### Skills

- Python
- FastAPI
- Machine Learning
- Scikit-learn
- Pandas
- SQL
- Power BI

---

## License

This project is licensed under the MIT License.


