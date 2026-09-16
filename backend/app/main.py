from fastapi import FastAPI, HTTPException
from sqlalchemy import text

from app.database import engine
from app.schemas import SessionCreateRequest, SquatCheckRequest
from app.services.validation import validate_session

app = FastAPI(title="Squat Form Analyzer API")

@app.get("/")
def home():
    return {"message": "Squat Form Analyzer API is running"}

@app.get("/api/database")
def check_database():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

    return {"database": result.scalar() == 1}

@app.post("/api/check")
def check_squat(data: SquatCheckRequest):
    return {
        "knee_angle_received": data.knee_angle,
        "torso_angle_received": data.torso_angle,
    }

@app.post("/api/sessions")
def create_session(payload: SessionCreateRequest):
    try:
        validate_session(payload)
    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        )

    return {
        "message": "Session is valid",
        "session": payload.model_dump(mode="json"),
    }