from app.database.models.workout_plan import WorkoutPlan
from app.repositories.workout_plan import WorkoutPlanRepository
from app.schemas.workout_plan import GetWorkoutPlan, CreateWorkoutPlan


class WorkoutPlanService:
    def __init__(self, repository: WorkoutPlanRepository) -> None:
        self.repository = repository

    async def create(self, user_id: int, data: CreateWorkoutPlan) -> WorkoutPlan:
        return await self.repository.create(user_id=user_id, name=data.name, description=data.description)

    async def get_user_plan(self, user_id: int)->list[WorkoutPlan]:
        return await self.repository.get_by_user_id(user_id)