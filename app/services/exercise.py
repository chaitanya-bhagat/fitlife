from app.schemas.exercise import CreateExercise, GetExercise
from app.repositories.exercise import InMemoryExerciseRepository

class ExerciseService:
    def __init__(self, repository: InMemoryExerciseRepository) -> None:
        self.repository = repository

    def create(self, data: CreateExercise) -> GetExercise:
        return self.repository.create(data)