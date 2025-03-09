
import allure
import pytest

from framework.com_example_teamcity_api.enum.endpoit import Endpoint
from framework.com_example_teamcity_api.generators.test_data_generator import TestDataGenerator
from framework.com_example_teamcity_api.models.build_type import BuildType
from framework.com_example_teamcity_api.models.project import Project

from framework.com_example_teamcity_api.models.user import User
from framework.com_example_teamcity_api.requests.check.checked_base import CheckedBase
from framework.com_example_teamcity_api.spec.specification import Specification
from test.com_example_teamcity.base_api_test import BaseApiTest


@pytest.mark.regression
class TestBuildType(BaseApiTest):
    @pytest.mark.description("User should be able ti create build type")
    @pytest.mark.positive
    @pytest.mark.crud
    def test_user_creates_build_type(self):
        """Создаёт пользователя, проект, билд-тайп и проверяет успешное создание."""
        user = TestDataGenerator.generate(User)
        with allure.step("Create user"):
            session_req, base_uri = Specification.super_user_auth_spec()
            user_request = CheckedBase[User](session_req, base_uri, Endpoint.USERS)
            user_request.create(user)
        project = TestDataGenerator.generate(Project)
        with allure.step("Create project by user"):
            session_req, base_uri = Specification.auth_spec(user)
            project_request = CheckedBase[Project](session_req, base_uri, Endpoint.PROJECTS)
            response = project_request.create(project)
            project_id = response.id
        build_type = TestDataGenerator.generate(BuildType)
        build_type.project = Project(id=project_id)
        session_req, base_uri = Specification.auth_spec(user)
        build_type_request = CheckedBase[BuildType](session_req, base_uri, Endpoint.BUILD_TYPES)
        with allure.step("Create build type for project by user"):
            build_type_id = build_type_request.create(build_type).id
        with allure.step("Check build type was created successfully with correct data"):
            created_build_type  = build_type_request.read(build_type_id)
            self.softy.assert_equal(build_type.name, created_build_type.name, msg="билд тайп имя не корреткно")

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
