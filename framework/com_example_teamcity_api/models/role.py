from dataclasses import dataclass

from framework.com_example_teamcity_api.models.base_model import BaseModel

@dataclass
class Role(BaseModel):
    roleId: str = "SYSTEM_ADMIN"
    scope: str = "g"