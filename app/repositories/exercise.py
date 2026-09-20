from app.schemas.exercise import CreateExercise,GetExercise

class InMemoryExerciseRepository:
    def __init__(self) -> None:
        self._items: dict[int, GetExercise] = {}
        self._next_id: int = 1

    def create(self, data: CreateExercise) -> GetExercise:
        exercise = GetExercise(
            id = self._next_id,
            **data.model_dump(),
        )
        self._items[self._next_id] = exercise
        self._next_id +=1

        return exercise

    def list(self) -> list[GetExercise]:
        return list(self._items.values())

    def get(self, exercise_id: int) -> GetExercise | None:
        return self._items.get(exercise_id)
