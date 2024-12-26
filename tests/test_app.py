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
