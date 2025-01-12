from http import HTTPStatus


def test_read_root_is_ok_and_ola_mundo(client):
    response = client.get('/')  # Act (Ação do teste)

    assert response.status_code == HTTPStatus.OK  # Assert (Verificação do resultado)
    assert response.json() == {
        'message': 'Olá mundo'
    }  # Assert (Verificação do resultado)


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    # Return the correct status code?
    assert response.status_code == HTTPStatus.CREATED
    # Validate the response body?
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')  # Act (Ação do teste)

    assert response.status_code == HTTPStatus.OK  # Assert (Verificação do resultado)
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testeusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testeusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
