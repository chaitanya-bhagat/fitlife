from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.repositories.exercise import ExerciseRepository
from app.services.exercise import ExerciseService
from app.schemas.exercise import CreateExercise, GetExercise


router = APIRouter(
    prefix="/exercises",
    tags=["exercises"]
)

def get_exercise_service(
        db: AsyncSession = Depends(get_db)
) -> ExerciseService:
    repository = ExerciseRepository(db)
    return ExerciseService(repository)

@router.post("", response_model=GetExercise, status_code=status.HTTP_201_CREATED)
async def create_exercise(payload: CreateExercise, service: ExerciseService = Depends(get_exercise_service)) -> GetExercise:
    return await service.create(payload)

@router.get("/{exercise_id}", response_model=GetExercise)
async def get_exercise(exercise_id: int, service: ExerciseService = Depends(get_exercise_service)) -> GetExercise:
    exercise =await service.get(exercise_id)
    if exercise is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercise not found"
        )
    return exercise

@router.get("", response_model=list[GetExercise])
async def list_exercises(service: ExerciseService = Depends(get_exercise_service)) -> list[GetExercise]:
    return await service.list()


