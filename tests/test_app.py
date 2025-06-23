from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'usernametest',
            'email': 'emailtest@test.com',
            'password': 'passwordtest',
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


def test_read_users(client):
    response = client.get('/users/')

    response_code = response.status_code
    response_json = response.json()

    assert response_code == HTTPStatus.OK
    assert response_json == {
        'users': [
            {
                'username': 'usernametest',
                'email': 'emailtest@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword'
        }
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
