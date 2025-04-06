from dataclasses import field

from pydantic import Field

from framework.com_example_teamcity_api.models.base_model import BaseModelPD
from framework.com_example_teamcity_api.models.project import Project
from framework.com_example_teamcity_api.models.steps import Steps


class BuildType(BaseModelPD):
    id: str = ""
    name: str = ""
    project: Project = Field(default_factory=Project)
    steps: Steps = Field(default_factory=Steps)