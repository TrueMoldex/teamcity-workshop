from attr import dataclass

from framework.com_example_teamcity_api.models.base_model import BaseModel


@dataclass
class Step(BaseModel):
    id: str
    name: str
    type: str = "simpleRunner"
