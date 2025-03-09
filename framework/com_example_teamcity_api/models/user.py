from attr import dataclass, asdict
from framework.com_example_teamcity_api.models.base_model import BaseModel


@dataclass
class User(BaseModel):
    username: str
    password: str

    def to_dict(self):
        return asdict(self)