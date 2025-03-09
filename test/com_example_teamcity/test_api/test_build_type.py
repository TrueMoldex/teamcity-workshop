import pytest


@pytest.mark.regression
class TestBuildType:
    @pytest.mark.description("User should be able ti create build type")
    @pytest.mark.positive
    @pytest.mark.CRUD
    def test_user_creates_build_type(self):
        """Создаёт пользователя, проект, билд-тайп и проверяет успешное создание."""
        # создать пользователя
        # создать проект
        # создать билд тайп
        # проверть что билд type создался успешно
        # @allure.step("Create user")
        # pass
        # @allure.step("Create project by user")
        # pass
        # @allure.step("Create build type for project by user")
        # pass
        # @allure.step("Check build type was created successfully with correct data")
        pass

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