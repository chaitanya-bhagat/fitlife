from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models.workout_plan import WorkoutPlan
from sqlalchemy import select


class WorkoutPlanRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(
        self, user_id: int, name: str, description: str | None
    ) -> WorkoutPlan:
        plan = WorkoutPlan(
            user_id=user_id,
            name=name,
            description=description,
        )

        self.session.add(plan)
        await self.session.commit()
        await self.session.refresh(plan)
        return plan

    async def get_by_user_id(self, user_id: int) -> list[WorkoutPlan]:
        statement = (
            select(WorkoutPlan)
            .where(WorkoutPlan.user_id == user_id)
            .order_by(WorkoutPlan.id.desc())
        )
        result = await self.session.execute(statement)
        return list(result.scalars().all())

    async def get_by_id(self, plan_id: int, user_id: int) -> WorkoutPlan | None:
        statement = select(WorkoutPlan).where(
            WorkoutPlan.id == plan_id,
            WorkoutPlan.user_id == user_id,
        )
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def update(self, plan: WorkoutPlan, changes: dict)->WorkoutPlan:
        for field, value in changes.items():
            setattr(plan, field, value)

        await self.session.commit()
        await self.session.refresh(plan)
        return plan

    async def delete(self, plan: WorkoutPlan) -> None:
        await self.session.delete(plan)
        await self.session.commit()