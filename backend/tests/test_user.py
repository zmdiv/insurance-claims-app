import unittest
from mockito import when, verify, unstub, mock
from app.services.user_service import UserService
from app.models.user import User
from app.schemas import UserCreate

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        self.user = UserCreate(email="test@example.com", password="password")
        self.db_session = mock()

    def test_create_user(self):
        db_user = User(email=self.user.email, hashed_password=self.user.password)
        when(self.db_session).add(...).thenReturn(None)
        when(self.db_session).commit().thenReturn(None)
        when(self.db_session).refresh(...).thenReturn(db_user)

        result = self.user_service.create_user(self.db_session, self.user)

        verify(self.db_session).add(...)
        verify(self.db_session).commit()
        verify(self.db_session).refresh(...)
        self.assertIsNotNone(result)
        self.assertEqual(result.email, "test@example.com")
        self.assertEqual(result.hashed_password, "password")

    def tearDown(self):
        unstub()

if __name__ == "__main__":
    unittest.main()
