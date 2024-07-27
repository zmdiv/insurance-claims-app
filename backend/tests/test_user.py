import unittest
from mockito import mock, when, verify
from app.services.user_service import UserService
from app.models.user import User

class TestUserService(unittest.TestCase):
    def test_create_user(self):
        user_service = UserService()
        user = mock(User)
        
        when(user).email.thenReturn("test@example.com")
        when(user).password.thenReturn("password")

        result = user_service.create_user(user)

        verify(user, times=1).email
        verify(user, times=1).password
        self.assertIsNotNone(result)
