import time

from framework.com_example_teamcity_api.enum.endpoit import Endpoint
from framework.com_example_teamcity_api.models.build import Build
from framework.com_example_teamcity_api.requests.check.checked_base import CheckedBase
from framework.com_example_teamcity_api.spec.specification import Specification
from test.com_example_teamcity.base_test import BaseTest


class TestBuildStart(BaseTest):
    def test_user_starts_build_with_mock(self):
        """Проверяет, что пользователь может запустить билд (через мок-сервер)."""
        checked_build_queue_request = CheckedBase(
            *Specification.mock_spec(), Endpoint.BUILD_QUEUE
        )

        build = checked_build_queue_request.create(
            Build(id="some_build_id", state="finished", status="SUCCESS")
        )

        self.softy.assert_equal(build.state, "finished", "Build state is correct")
        self.softy.assert_equal(build.status, "SUCCESS", "Build status is correct")
