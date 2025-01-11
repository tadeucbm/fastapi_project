from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_is_ok_and_ola_mundo():
    client = TestClient(app)  # Arrange (Organização do teste)

    response = client.get('/')  # Act (Ação do teste)

    assert response.status_code == HTTPStatus.OK  # Assert (Verificação do resultado)
    assert response.json() == {
        'message': 'Olá mundo'
    }  # Assert (Verificação do resultado)


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        }
    )

    # Return the correct status code?
    assert response.status_code == HTTPStatus.CREATED
    # Validate the response body?
    assert response.json() == {
            'username': 'testusername',
            'email': 'test@test.com',
            'id': 1,
    }
