from unittest import TestCase

from app.domains.models import User


class TestModels(TestCase):
    def test_given_that_the_parameters_are_valid_when_the_new_instance_from_user_to_created_then_user_must_be_created(
            self
    ):
        user = User()
        user.email = 'asdfsdafsdaf'
        user.hashed_password = 'bhbasdfsdafsdaf'
