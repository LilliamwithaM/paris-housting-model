from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI(title='Paris Housing Price Prediction')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model = load(pathlib.Path('model/paris-housing-v1.joblib'))

class InputData(BaseModel):
    squareMeters: int = 55712
    numberOfRooms: int = 58
    hasYard: int = 0
    hasPool: int = 1
    floors: int = 19
    cityCode: int = 34457
    cityPartRange: int = 6
    numPrevOwners: int = 8
    made: int = 2021
    isNewBuilt: int = 0
    hasStormProtector: int = 0
    basement: int = 2937
    attic: int = 8852
    garage: int = 135
    hasStorageRoom: int = 1
    hasGuestRoom: int = 9
    price: float = 5574642.1

class OutputData(BaseModel):
    score: float = 4993447.5

@app.post('/score', response_model=OutputData)
def score(data: InputData):
    model_input = np.array([v for k, v in data.dict().items()]).reshape(1, -1)
    result = model.predict(model_input)  # Utiliza predict en lugar de predict_proba

    return {'score': result[0]}