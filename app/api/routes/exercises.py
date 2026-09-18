from fastapi import APIRouter, status

from app.repositories.exercise import InMemoryExerciseRepository
from app.services.exercise import ExerciseService
from app.schemas.exercise import CreateExercise, GetExercise


router = APIRouter(
    prefix="/exercises",
    tags=["exercises"]
)

repository = InMemoryExerciseRepository()
service = ExerciseService(repository)

@router.post("", response_model=GetExercise, status_code=status.HTTP_201_CREATED)
async def create_exercise(payload: CreateExercise) -> GetExercise:
    return service.create(payload)


