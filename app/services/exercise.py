from app.schemas.exercise import CreateExercise, GetExercise, UpdateExercise
from app.repositories.exercise import ExerciseRepository
from app.database.models.exercise import Exercise


class ExerciseService:
    def __init__(self, repository: ExerciseRepository) -> None:
        self.repository = repository

    async def create(self, data: CreateExercise) -> Exercise:
        return await self.repository.create(data)

    async def get(self, exercise_id) -> Exercise:
        return await self.repository.get(exercise_id)

    async def list(self) -> list[GetExercise]:
        return await self.repository.list()

    async def update(self, exercise_id: int, data: UpdateExercise) -> Exercise | None:
        return await self.repository.update(exercise_id, data)

    async def delete(self, exercise_id: int) -> bool:
        return await self.repository.delete(exercise_id)
