from typing import TypeVar, Generic
from dataclasses import fields
import logging
from framework.com_example_teamcity_api.enum.endpoit import Endpoint
from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.requests.crud_interaface import CRUDInterface
from framework.com_example_teamcity_api.requests.request import Request
import requests

from framework.com_example_teamcity_api.requests.uncheck.unchecked_base import UncheckedBase

T = TypeVar("T", bound=BaseModel)

class CheckedBase(Request, CRUDInterface, Generic[T]):
    def __init__(self, spec, base_uri, endpoint: Endpoint):
        super().__init__(spec, endpoint)
        self.base_uri = base_uri
        self.unchecked_base = UncheckedBase(spec, base_uri, endpoint)

    def _validate_and_extract(self, response, model_class: type[T]) -> T:
        if response.status_code != requests.codes.ok:
            logging.error(f"❌ Ошибка {response.status_code}: {response.text}")
            raise Exception(f"Unexpected status code: {response.status_code}, Response: {response.text}")
        logging.info(f"✅ Успешный ответ: {response.status_code}, Тело: {response.text}")
        if model_class:
            data = response.json()
            allowed_fields = {field.name for field in fields(model_class)}
            filtered_data = {k: v for k, v in data.items() if k in allowed_fields}
            return model_class(**filtered_data)
        else:
            return response.text

    def create(self, model: BaseModel) -> T:
        response = self.unchecked_base.create(model)
        return self._validate_and_extract(response, self.endpoint.model_class)

    def read(self, ids: str) -> T:
        response = self.unchecked_base.read(ids)
        return self._validate_and_extract(response, self.endpoint.model_class)

    def update(self, ids: str, model: BaseModel) -> T:
        response = self.unchecked_base.update(ids, model)
        return self._validate_and_extract(response, self.endpoint.model_class)

    def delete(self, ids: str) -> str:
        response = self.unchecked_base.delete(ids)
        return self._validate_and_extract(response, None)