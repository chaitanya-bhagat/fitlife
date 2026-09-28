from pydantic import BaseModel, Field, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)


class UpdateExercise(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    muscle_group: MuscleGroup | None = None
    difficulty: Difficulty | None = None
    equipment: str | None = Field(default=None, max_length=100)
    instruction: str | None = Field(default=None, max_length=2000)
