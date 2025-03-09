from dataclasses import dataclass, field
from typing import List

from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.models.role import Role


@dataclass
class Roles(BaseModel):
    role: List[Role] = field(default_factory=lambda: [Role()])