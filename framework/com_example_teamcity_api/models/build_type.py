from dataclasses import dataclass

from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.models.project import Project
from framework.com_example_teamcity_api.models.steps import Steps


@dataclass
class BuildType(BaseModel):
    id: str
    name: str
    project: Project
    steps: Steps
