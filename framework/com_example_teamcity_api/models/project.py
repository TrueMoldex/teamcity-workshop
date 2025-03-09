from dataclasses import dataclass, field, asdict

from attr import dataclass

from framework.com_example_teamcity_api.models.base_model import BaseModel


@dataclass
class Project(BaseModel):
  id: str = field(default="", metadata={"random": True})
  name: str = field(default="", metadata={"random": True})
  location: str = "_Root"