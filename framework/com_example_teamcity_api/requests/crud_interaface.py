from abc import ABC, abstractmethod

from framework.com_example_teamcity_api.models.base_model import BaseModel


class CRUDInterface(ABC):

    @abstractmethod
    def create(self, model: BaseModel):
        pass

    @abstractmethod
    def read(self, ids: str):
        pass

    @abstractmethod
    def update(self, ids: str, model: BaseModel):
        pass
    
    @abstractmethod
    def delete(self, ids: str):
        pass