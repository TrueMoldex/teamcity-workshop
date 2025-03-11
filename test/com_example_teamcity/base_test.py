import pytest

from framework.com_example_teamcity_api.requests.check_request import CheckedRequests
from framework.com_example_teamcity_api.spec.specification import Specification
from test.com_example_teamcity.soft_assert import SoftAssert


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Создаёт soft assertions перед каждым тестом и выполняет assert_all() после."""
        self.softy = SoftAssert()
        yield
        self.softy.assert_all()

    @classmethod
    def setup_class(cls):
        """Инициализация суперпользовательских запросов один раз перед всеми тестами."""
        session, base_uri = Specification.super_user_auth_spec()

        # Проверяем, сколько аргументов принимает CheckedRequests
        try:
            cls.super_user_check_requests = CheckedRequests(session, base_uri)
        except TypeError:
            cls.super_user_check_requests = CheckedRequests(session)