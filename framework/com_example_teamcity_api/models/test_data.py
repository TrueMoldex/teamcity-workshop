from pydantic import Field

from framework.com_example_teamcity_api.models.base_model import BaseModelPD
from framework.com_example_teamcity_api.models.build_type import BuildType
from framework.com_example_teamcity_api.models.project import Project
from framework.com_example_teamcity_api.models.user import User


class TestData(BaseModelPD):
    project: Project = Field(default_factory=Project)
    user: User = Field(default_factory=User)
    build_type: BuildType = Field(default_factory=BuildType)