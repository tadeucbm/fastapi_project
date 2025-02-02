from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='testuser', password='testpassword', email='test@mail.com')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'test@mail.com'))

    assert result.id == 1
