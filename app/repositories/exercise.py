from app.schemas.exercise import CreateExercise

from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models.exercise import Exercise
from sqlalchemy import select


class ExerciseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, data: CreateExercise) -> Exercise:
        exercise = Exercise(
            name=data.name,
            muscle_group=data.muscle_group.value,
            difficulty=data.difficulty.value,
            equipment=data.equipment,
            instruction=data.instruction,
        )
        self.session.add(exercise)
        await self.session.commit()
        await self.session.refresh(exercise)
        return exercise

    async def get(self, exercise_id: int) -> Exercise:
        return await self.session.get(Exercise, exercise_id)

    async def list(self) -> list[Exercise]:
        statement = select(Exercise)
        result = await self.session.execute(statement)
        return list(result.scalars().all())


