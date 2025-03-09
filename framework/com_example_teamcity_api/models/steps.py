from attr import dataclass

from framework.com_example_teamcity_api.models.base_model import BaseModel


@dataclass
class Steps(BaseModel):
  count: int
  step: list