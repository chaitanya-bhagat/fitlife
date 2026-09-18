from pydantic import BaseModel, Field
from enum import StrEnum


class MuscleGroup(StrEnum):
    CHEST = "chest"
    BACK = "back"
    LEGS = "legs"

class Difficulty(StrEnum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediat"
    ADVANCED = "advanced"

class ExerciseBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    muscle_group: MuscleGroup
    difficulty: Difficulty
    equipment: str | None = None
    instruction: str | None = None

class CreateExercise(ExerciseBase):
    pass

class GetExercise(ExerciseBase):
    id: int

