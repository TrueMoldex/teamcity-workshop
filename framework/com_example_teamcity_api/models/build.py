from dataclasses import dataclass

from framework.com_example_teamcity_api.models.base_model import BaseModel


@dataclass
class Build(BaseModel):
    state: str
    status: str
    id : str  = ''
