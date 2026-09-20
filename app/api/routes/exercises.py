from fastapi import APIRouter, status, Depends, HTTPException

from app.repositories.exercise import InMemoryExerciseRepository
from app.services.exercise import ExerciseService
from app.schemas.exercise import CreateExercise, GetExercise


router = APIRouter(
    prefix="/exercises",
    tags=["exercises"]
)

repository = InMemoryExerciseRepository()
# service = ExerciseService(repository)

def get_exercise_service() -> ExerciseService:
    return ExerciseService(repository)

@router.post("", response_model=GetExercise, status_code=status.HTTP_201_CREATED)
async def create_exercise(payload: CreateExercise, service: ExerciseService = Depends(get_exercise_service)) -> GetExercise:
    return service.create(payload)

@router.get("", response_model=list[GetExercise])
async def list_exercises(service: ExerciseService = Depends(get_exercise_service)) -> list[GetExercise]:
    return service.list()

@router.get("/{exercise_id}", response_model=GetExercise)
async def get_exercise(exercise_id: int, service : ExerciseService = Depends(get_exercise_service)) -> GetExercise:
    exercise =  service.get(exercise_id)
    if exercise is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercise not found"
        )

    return exercise


