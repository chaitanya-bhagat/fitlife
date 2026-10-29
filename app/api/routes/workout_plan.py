from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies.auth import get_current_user
from app.database.models.user import User
from app.database.session import get_db
from app.repositories.workout_plan import WorkoutPlanRepository
from app.services.workout_plan import WorkoutPlanService
from app.schemas.workout_plan import GetWorkoutPlan, CreateWorkoutPlan

router = APIRouter(
    prefix="/workout-plans",
    tags=["workout-plans"],
)


def get_workout_plan_service(db: AsyncSession = Depends(get_db)) -> WorkoutPlanService:
    repository = WorkoutPlanRepository(db)
    return WorkoutPlanService(repository)


@router.post("", response_model=GetWorkoutPlan, status_code=status.HTTP_201_CREATED)
async def create_workout_plan(
    payload: CreateWorkoutPlan,
    current_user: User = Depends(get_current_user),
    service: WorkoutPlanService = Depends(get_workout_plan_service),
) -> GetWorkoutPlan:
    return await service.create(
        user_id=current_user.id,
        data=payload
    )
