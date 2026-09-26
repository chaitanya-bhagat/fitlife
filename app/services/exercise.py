from app.schemas.exercise import CreateExercise, GetExercise
from app.repositories.exercise import InMemoryExerciseRepository, ExerciseRepository
from app.database.models.exercise import Exercise

class ExerciseService:
    def __init__(self, repository: ExerciseRepository) -> None:
        self.repository = repository

    async def create(self, data: CreateExercise) -> Exercise:
        return await self.repository.create(data)
        
    def list(self) -> list[GetExercise]:
        return self.repository.list() 

    def get(self, exercise_id: int) -> GetExercise:
        return self.repository.get(exercise_id)