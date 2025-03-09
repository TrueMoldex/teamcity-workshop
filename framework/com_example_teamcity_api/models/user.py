from dataclasses import dataclass, field, asdict
from framework.com_example_teamcity_api.models.base_model import BaseModel


@dataclass
class User(BaseModel):
    username: str = field(default= "", metadata={"random": True})
    password: str = field(default="", metadata={"random": True})

    def to_dict(self):
        return asdict(self)