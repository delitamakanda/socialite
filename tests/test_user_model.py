import unittest
from app.models import User, Permission, Role, AnonymousUser

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'toto')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password = 'toto')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'toto')
        self.assertTrue(u.verify_password('toto'))
        self.assertFalse(u.verify_password('tata'))

    def test_password_salts_are_random(self):
        u = User(password = 'toto')
        u2 = User(password = 'tata')
        self.assertTrue(u.password_hash != u2.password_hash)


    def test_roles_and_permissions(self):
        Role.insert_roles()
        u = User(email="john.doe@example.com", password='toto')
        self.assertTrue(u.can(Permission.WRITE_ARTICLES))
        self.assertFalse(u.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
