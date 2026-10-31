from fastapi import FastAPI

from app.api.routes.exercises import router as exercise_router
from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.api.routes.workout_plan import router as workout_plan_router

app = FastAPI()

app.include_router(exercise_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(workout_plan_router)