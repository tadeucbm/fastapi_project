from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app import app


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'usernametest',
            'email': 'emailtest@test.com',
            'password': 'passwordtest'
        },
    )

    response_code = response.status_code
    response_json = response.json()

    assert response_code == HTTPStatus.CREATED
    assert response_json == {
        'id': 1,
        'username': 'usernametest',
        'email': 'emailtest@test.com',
    }
