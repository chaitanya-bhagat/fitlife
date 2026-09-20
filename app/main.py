from fastapi import FastAPI

from app.api.routes.exercises import router as exercise_router

app = FastAPI()

app.include_router(exercise_router)