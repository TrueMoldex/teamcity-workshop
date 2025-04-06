from typing import List

from pydantic import Field

from framework.com_example_teamcity_api.models.base_model import BaseModelPD
from framework.com_example_teamcity_api.models.role import Role


class Roles(BaseModelPD):
    role: List[Role] = Field(default_factory=lambda: [Role()])
