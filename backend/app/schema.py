from pydantic import BaseModel, Field


class SquatCheckRequest(BaseModel):
    knee_angle: float = Field(ge=0, le=180)
    torso_angle: float = Field(ge=0, le=180)