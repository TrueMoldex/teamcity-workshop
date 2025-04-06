from typing import List

from pydantic import Field

from framework.com_example_teamcity_api.models.base_model import BaseModelPD
from framework.com_example_teamcity_api.models.step import Step


class Steps(BaseModelPD):
    step: List[Step] = Field(default_factory=list)
    count: int = 0