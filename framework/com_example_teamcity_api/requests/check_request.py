from typing import TypeVar, Dict
from framework.com_example_teamcity_api.enum.endpoit import Endpoint
from framework.com_example_teamcity_api.requests.check.checked_base import CheckedBase
from framework.com_example_teamcity_api.models.base_model import BaseModel


T = TypeVar("T", bound=BaseModel)

class CheckedRequests:
    def __init__(self, spec, base_uri):
        self.requests: Dict[Endpoint, CheckedBase] = {
            endpoint: CheckedBase(spec, base_uri, endpoint) for endpoint in Endpoint
        }

    def get_request(self, endpoint: Endpoint) -> CheckedBase[T]:
        return self.requests[endpoint]