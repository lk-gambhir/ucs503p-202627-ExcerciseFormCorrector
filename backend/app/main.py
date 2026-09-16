from fastapi import FastAPI
from app.schema import SquatCheckRequest

app = FastAPI(title="Squat Form Analyzer API")

@app.get("/")
def home():
    return {"message": "Squat Form Analyzer API is running"}

@app.post("/api/check")
def check_squat(data: SquatCheckRequest):
    return {
        "knee_angle_received": data.knee_angle,
        "torso_angle_received": data.torso_angle,
    }