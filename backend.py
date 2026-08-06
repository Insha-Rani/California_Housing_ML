from fastapi import FastAPI

from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Literal
import pandas as pd
from model.ML_model import model, pipeline

class InputData(BaseModel):
    median_income: float = Field(...,gt=0.0,le=15.0, description="Median income of the household")
    total_rooms: float = Field(...,gt=0, description="Total number of rooms")
    total_bedrooms: float = Field(...,gt=0, description="Total number of bedrooms")
    population: float = Field(...,gt=0, description="Total population")
    households: float = Field(...,gt=0, description="Total number of households")
    latitude: float = Field(..., gt = 32.0, lt = 42.0, description="Latitude of the location")
    longitude: float = Field(..., gt = -125.0, lt = -114.0, description="Longitude of the location")
    ocean_proximity: Literal["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"] = Field(..., description="Proximity to the ocean")
    housing_median_age: float = Field(..., gt=0, description="Median age of the houses in the area")

    # 1. Field Validator Example: Check if rooms/bedrooms are reasonable
    @field_validator("housing_median_age")
    @classmethod
    def validate_age(cls, v: float) -> float:
        if v < 1:
            raise ValueError("Housing median age must be at least 1 year.")
        return v

    # 2. Model Validator Example: Cross-field validation (bedrooms <= total_rooms)
    @model_validator(mode="after")
    def check_bedrooms_less_than_rooms(self):
        if self.total_bedrooms > self.total_rooms:
            raise ValueError(
                f"total_bedrooms ({self.total_bedrooms}) cannot be greater than total_rooms ({self.total_rooms})."
            )
        return self

    @field_validator("ocean_proximity", mode="before")
    @classmethod
    def convert_to_uppercase(cls, v: str) -> str:
        if isinstance(v, str):
            return v.upper()
        return v

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Housing Price Prediction API!"}

@app.post("/predict")
def predict(input_data: InputData):
    input_df = pd.DataFrame([input_data.dict()])
    transformed_input = pipeline.transform(input_df)
    prediction = model.predict(transformed_input)
    return {"predicted_median_house_value": prediction[0]}