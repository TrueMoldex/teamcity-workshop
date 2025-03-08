import logging

from framework.com_example_teamcity_api.models.user import User
from framework.com_example_teamcity_api.spec.specification import Specification

logging.basicConfig(level=logging.INFO)

class TestDummy():
    def test_user_should_be_able_get_all_projects(self):
        spec = Specification()
        user = User(user="admin", password="admin")
        spec.auth_spec_request(user=user, endpoint="/app/rest/projects")
