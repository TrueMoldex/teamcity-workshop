from framework.com_example_teamcity_api.enum.endpoit import Endpoint
from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.requests.crud_interaface import CRUDInterface
from framework.com_example_teamcity_api.requests.request import Request
import requests

from framework.com_example_teamcity_api.requests.uncheck.unchecked_base import UncheckedBase


class CheckedBase(Request, CRUDInterface):

    def __init__(self, spec, endpoint: Endpoint):
        super().__init__(spec, endpoint)
        self.unchecked_base = UncheckedBase(spec, endpoint)

    def _validate_and_extract(self, response, model_class):
        if response.status_code != requests.codes.ok:
            raise Exception(f"Unexpected status code: {response.status_code}, Response: {response.text}")
        return response.json() if model_class else response.text

    def create(self, model: BaseModel):
        response = self.unchecked_base.create(model)
        return self._validate_and_extract(response, self.endpoint.model_class)

    def read(self, ids: str):
        response = self.unchecked_base.read(ids)
        return self._validate_and_extract(response, self.endpoint.model_class)

    def update(self, ids: str, model: BaseModel):
        response = self.unchecked_base.update(ids, model)
        return self._validate_and_extract(response, self.endpoint.model_class)

    def delete(self, ids: str):
        response = self.unchecked_base.delete(ids)
        return self._validate_and_extract(response, None)
