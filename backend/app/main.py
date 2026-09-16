from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Squat Form Analyzer API")


class HealthResponse(BaseModel):
    status: str


class SquatCheckRequest(BaseModel):
    knee_angle: float = Field(ge=0, le=180)
    torso_angle: float = Field(ge=0, le=180)


@app.get("/api/health", response_model=HealthResponse)
def health():
    return {"status": "ok"}


@app.post("/api/check")
def check_squat(payload: SquatCheckRequest):
    issues = []

    if payload.knee_angle > 100:
        issues.append("Go deeper")

    if payload.torso_angle > 55:
        issues.append("Keep your chest more upright")

    score = max(0, 100 - len(issues) * 25)

    return {
        "score": score,
        "issues": issues,
    }