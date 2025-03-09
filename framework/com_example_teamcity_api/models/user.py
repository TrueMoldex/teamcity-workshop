from dataclasses import dataclass, field, asdict
from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.models.roles import Roles


@dataclass
class User(BaseModel):
    username: str = field(default= "", metadata={"random": True})
    password: str = field(default="", metadata={"random": True})
    roles: Roles = field(default_factory=Roles)
    def to_dict(self):
        return asdict(self)