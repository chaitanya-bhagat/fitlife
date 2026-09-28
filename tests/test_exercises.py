from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_exercise() -> None:
    create_response = client.post(
        "/exercises",
        json={
            "name": "Bench Press",
            "muscle_group": "chest",
            "difficulty": "beginner",
            "equipment": "barbell",
        },
    )

    assert create_response.status_code == 201

    created = create_response.json()
    exercise_id = created["id"]

    get_response = client.get(
        f"/exercises/{exercise_id}",
    )

    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Bench Press"

def test_get_exercise_not_found() ->None:
    response = client.get(
        f"/exercises/123"
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail":"Exercise not found"
    }




