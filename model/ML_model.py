import joblib
model_file = "model\\model.pkl"
Pipeline_file = "model\\pipeline.pkl"


model = joblib.load(model_file)
pipeline = joblib.load(Pipeline_file)