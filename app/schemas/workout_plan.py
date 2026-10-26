from pydantic import BaseModel, ConfigDict, Field

class CreateWorkoutPlan(BaseModel):
    name: str = Field(min_length=3, max_length=150)
    description: str | None = None

class GetWorkoutPlan(BaseModel):
    id: int 
    user_id: int
    name: str
    description: str | None

    model_config = ConfigDict(from_attributes=True)
