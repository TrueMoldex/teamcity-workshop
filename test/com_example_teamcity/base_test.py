import pytest

from framework.com_example_teamcity_api.generators.test_data_generator import TestDataGenerator
from framework.com_example_teamcity_api.generators.test_data_storage import TestDataStorage
from framework.com_example_teamcity_api.requests.check_request import CheckedRequests
from framework.com_example_teamcity_api.spec.specification import Specification
from test.com_example_teamcity.soft_assert import SoftAssert


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.softy = SoftAssert()
        self.test_data = TestDataGenerator.generate_test_data()
        yield
        self.softy.assert_all()
        TestDataStorage().delete_created_entities()

    @classmethod
    def setup_class(cls):
        """Инициализация суперпользовательских запросов один раз перед всеми тестами."""
        session, base_uri = Specification.super_user_auth_spec()

        try:
            cls.super_user_check_requests = CheckedRequests(session, base_uri)
        except TypeError:
            cls.super_user_check_requests = CheckedRequests(session)