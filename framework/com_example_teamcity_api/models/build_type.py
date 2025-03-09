from dataclasses import dataclass, field

from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.models.project import Project
from framework.com_example_teamcity_api.models.steps import Steps


@dataclass
class BuildType(BaseModel):
    id: str = field(default="", metadata={"random": True})
    name: str = field(default="", metadata={"random": True})
    project: Project = field(default_factory=Project)
    steps: Steps = field(default_factory=Steps)
