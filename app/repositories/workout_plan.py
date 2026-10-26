from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models.workout_plan import WorkoutPlan

class WorkoutPlanRepository:
    def __init__(self, session: AsyncSession)->None:
        self.session = session

    async def create(self, user_id: int, name: str, description: str|None)->WorkoutPlan:
        plan= WorkoutPlan(
            user_id=user_id,
            name=name,
            description=description,
        )

        self.session.add(plan)
        await self.session.commit()
        await self.session.refresh(plan)
        return plan

        
