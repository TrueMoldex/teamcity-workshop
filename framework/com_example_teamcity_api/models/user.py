from dataclasses import asdict
from typing import Optional

from pydantic import Field

from framework.com_example_teamcity_api.models.base_model import BaseModelPD
from framework.com_example_teamcity_api.models.roles import Roles


class User(BaseModelPD):
    id: Optional[str] = None
    username: str = ""
    password: str = ""
    roles: Roles = Field(default_factory=Roles)

    # def to_dict(self):
    #     return asdict(self)