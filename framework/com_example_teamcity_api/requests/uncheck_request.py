from framework.com_example_teamcity_api.enum.endpoit import Endpoint
from framework.com_example_teamcity_api.requests.uncheck.unchecked_base import (
    UncheckedBase,
)


class UncheckedRequests:
    def __init__(self, spec, base_uri):
        self.requests = {}
        for endpoint in Endpoint:
            self.requests[endpoint] = UncheckedBase(spec, base_uri, endpoint)

    def get_request(self, endpoint: Endpoint) -> UncheckedBase:
        return self.requests[endpoint]
