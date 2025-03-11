
import allure
import pytest

from framework.com_example_teamcity_api.enum.endpoit import Endpoint
from framework.com_example_teamcity_api.generators.test_data_generator import TestDataGenerator
from framework.com_example_teamcity_api.models.build_type import BuildType
from framework.com_example_teamcity_api.models.project import Project

from framework.com_example_teamcity_api.models.user import User
from framework.com_example_teamcity_api.requests.check.checked_base import CheckedBase
from framework.com_example_teamcity_api.requests.check_request import CheckedRequests
from framework.com_example_teamcity_api.spec.specification import Specification
from test.com_example_teamcity.base_api_test import BaseApiTest


@pytest.mark.regression
class TestBuildType(BaseApiTest):
    @pytest.mark.description("User should be able ti create build type")
    @pytest.mark.positive
    @pytest.mark.crud
    def test_user_creates_build_type(self):
        user = TestDataGenerator.generate(User)

        self.super_user_check_requests.get_request(Endpoint.USERS).create(user)

        user_requests = CheckedRequests(*Specification.auth_spec(user))

        project = TestDataGenerator.generate(Project)

        project = user_requests.get_request(Endpoint.PROJECTS).create(project)

        build_type = TestDataGenerator.generate(BuildType)
        build_type.project = project #По-другому не получается почему-то  404 и ошибку с локатором вывыодит
        user_requests.get_request(Endpoint.BUILD_TYPES).create(build_type)

        created_build_type = user_requests.get_request(Endpoint.BUILD_TYPES).read(build_type.id)

        self.softy.assert_equal(build_type.name, created_build_type.name, "Build Type name is correct")

    @pytest.mark.description("User should not be able to create two build type with same id")
    @pytest.mark.negative
    @pytest.mark.crud
    def test_user_creates_two_build_types_with_the_same_id(self):
        """Создаёт пользователя, проект, два билд-тайпа с одинаковым id и проверяет, что второй не создаётся."""
        # создать пользователя
        # создать проект
        # создать билд тайп
        # создать второй билд тайп с id первого
        # проверть что билд type  не создался успешно
        # @allure.step("Create user")
        # pass
        # @allure.step("Create project by user")
        # pass
        # @allure.step("Create build type for project by user")
        # pass
        # @allure.step("Create build type for project by user with same id")
        # pass
        # @allure.step("Check build type was  not created with bad request")
        pass

    @pytest.mark.description("Project admin should be able to create build type for their project")
    @pytest.mark.positive
    @pytest.mark.roles
    def test_project_admin_creates_build_type(self):
        """Администратор проекта создаёт билд-тайп для своего проекта и проверяет успешное создание."""
        # @allure.step("Create user")
        # @allure.step("Create project")
        # @allure.step("Grant user PROJECT_ADMIN role in project")
        # @allure.step("Create build type for project1 by user(PROJECT_ADMIN)")
        # @allure.step("Check build type was created successfully")
        pass

    @pytest.mark.description("Project admin should not be able to create build type for not their project")
    @pytest.mark.negative
    @pytest.mark.roles
    def test_project_admin_creates_build_type_for_another_user_project(self):
        """Администратор проекта пытается создать билд-тайп для чужого проекта и проверяет, что операция запрещена."""
        # @allure.step("Create user1")
        # @allure.step("Create project1")
        # @allure.step("Grant user1 PROJECT_ADMIN role in project1")
        #
        # @allure.step("Create user2")
        # @allure.step("Create project2")
        # @allure.step("Grant user2 PROJECT_ADMIN role in project2")
        #
        # @allure.step("Create build type for project1 by user2(PROJECT_ADMIN)")
        # @allure.step("Check build type was not created with forbidden code")
        pass
