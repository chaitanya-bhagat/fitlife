from app.database.models.workout_plan import WorkoutPlan
from app.repositories.workout_plan import WorkoutPlanRepository
from app.schemas.workout_plan import (
    GetWorkoutPlan,
    CreateWorkoutPlan,
    UpdateWorkoutPlan,
)


class WorkoutPlanNotFoundError(Exception):
    pass


class WorkoutPlanService:
    def __init__(self, repository: WorkoutPlanRepository) -> None:
        self.repository = repository

    async def create(self, user_id: int, data: CreateWorkoutPlan) -> WorkoutPlan:
        return await self.repository.create(
            user_id=user_id, name=data.name, description=data.description
        )

    async def get_user_plan(self, user_id: int) -> list[WorkoutPlan]:
        return await self.repository.get_by_user_id(user_id)

    async def get_by_id(
        self,
        plan_id: int,
        user_id: int,
    ) -> WorkoutPlan:
        plan = await self.repository.get_by_id(
            plan_id=plan_id,
            user_id=user_id,
        )

        if plan is None:
            raise WorkoutPlanNotFoundError()

        return plan

    async def update(
        self, plan_id: int, user_id: int, data: UpdateWorkoutPlan
    ) -> WorkoutPlan:
        plan = await self.repository.get_by_id(plan_id=plan_id, user_id=user_id)

        changes = data.model_dump(exclude_unset=True)
        if "name" in changes and changes["name"] is None:
            raise ValueError("Workout plan name can not be null")

        return await self.repository.update(plan=plan, changes=changes)

    async def delete(
        self,
        plan_id: int,
        user_id: int,
    ) -> None:
        plan = await self.get_by_id(
            plan_id=plan_id,
            user_id=user_id,
        )

        await self.repository.delete(plan)
