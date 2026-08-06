import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

with st.form("prediction_form"):
    st.title("Housing Price Prediction")
    
    median_income = st.number_input("Median Income", min_value=0.0, max_value=15.0, step=0.1)
    total_rooms = st.number_input("Total Rooms", min_value=1, step=1)
    total_bedrooms = st.number_input("Total Bedrooms", min_value=1, step=1)
    population = st.number_input("Population", min_value=1, step=1)
    households = st.number_input("Households", min_value=1, step=1)
    latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, step=0.01)
    longitude = st.number_input("Longitude", min_value=-125.0, max_value=-114.0, step=0.01)
    ocean_proximity = st.selectbox("Ocean Proximity", ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"])
    housing_median_age = st.number_input("Housing Median Age", min_value=1, step=1)

    submitted = st.form_submit_button("Predict")

    if submitted:
        input_data = {
            "median_income": median_income,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "latitude": latitude,
            "longitude": longitude,
            "ocean_proximity": ocean_proximity,
            "housing_median_age": housing_median_age
        }

        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            prediction = response.json()["predicted_median_house_value"]
            st.success(f"Predicted Median House Value: ${prediction:,.2f}")
        else:
            st.error(f"Error: {response.json()['detail']}")
