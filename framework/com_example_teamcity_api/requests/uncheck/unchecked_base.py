from framework.com_example_teamcity_api.enum.endpoit import Endpoint
from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.requests.crud_interaface import CRUDInterface
from framework.com_example_teamcity_api.requests.request import Request


class UncheckedBase(Request, CRUDInterface):
    def __init__(self, spec, endpoint: Endpoint):
        super().__init__(spec, endpoint)
        self.spec = spec  # Храним спецификацию для использования в методах

    def create(self, model: BaseModel):
        url = self.endpoint.url
        response = self.spec.session.post(url, json=model.to_dict(), headers=self.spec.default_headers)
        return response

    def read(self, ids: str):
        url = f"{self.endpoint.url}/id:{ids}"
        response = self.spec.session.get(url, headers=self.spec.default_headers)
        return response

    def update(self, ids: str, model: BaseModel):
        url = f"{self.endpoint.url}/id:{ids}"
        response = self.spec.session.put(url, json=model.to_dict(), headers=self.spec.default_headers)
        return response

    def delete(self, ids: str):
        url = f"{self.endpoint.url}/id:{ids}"
        response = self.spec.session.delete(url, headers=self.spec.default_headers)
        return response
