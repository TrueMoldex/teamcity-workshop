from framework.com_example_teamcity_api.enum.endpoit import Endpoint
from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.requests.crud_interaface import CRUDInterface
from framework.com_example_teamcity_api.requests.request import Request

import logging


class UncheckedBase(Request, CRUDInterface):
    def __init__(self, spec, base_uri, endpoint: Endpoint):
        super().__init__(spec, endpoint)
        self.base_uri = base_uri
        self.spec = spec

    def create(self, model: BaseModel):
        url = f"{self.base_uri}{self.endpoint.url}"
        payload = model.to_dict()
        logging.info(f"📡 Отправка запроса на: {url}")
        logging.info(f"📨 Данные: {payload}")
        response = self.spec.post(url, json=payload, headers=self.spec.headers)
        return response

    def read(self, ids: str):
        url = f"{self.base_uri}{self.endpoint.url}/id:{ids}"
        response = self.spec.get(url, headers=self.spec.headers)
        return response

    def update(self, ids: str, model: BaseModel):
        url = f"{self.base_uri}{self.endpoint.url}/id:{ids}"
        payload = model.to_dict()
        response = self.spec.put(url, json=payload, headers=self.spec.headers)
        return response

    def delete(self, ids: str):
        url = f"{self.base_uri}{self.endpoint.url}/id:{ids}"
        logging.info(f"📡 Отправка запроса на: {url}")
        response = self.spec.delete(url, headers=self.spec.headers)
        return response
