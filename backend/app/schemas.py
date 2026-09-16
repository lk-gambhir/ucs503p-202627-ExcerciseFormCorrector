from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class SquatCheckRequest(BaseModel):
    knee_angle: float = Field(ge=0, le=180)
    torso_angle: float = Field(ge=0, le=180)

class RepInput(BaseModel):
    rep_number: int = Field(ge=1)
    duration_seconds: float = Field(ge=0)
    rom_value: float = Field(ge=0)
    tempo: float = Field(ge=0)
    angle_metrics: dict[str, float] = Field(default_factory=dict)

class FormIssueInput(BaseModel):
    rep_number: int = Field(ge=1)
    issue_type: str
    severity: Severity

class SessionCreateRequest(BaseModel):
    exercise: str
    started_at: datetime
    ended_at: datetime
    duration_seconds: float = Field(ge=0)
    rep_count: int = Field(ge=0)
    form_score: float = Field(ge=0, le=100)
    reps: list[RepInput] = Field(default_factory=list)
    form_issues: list[FormIssueInput] = Field(default_factory=list)