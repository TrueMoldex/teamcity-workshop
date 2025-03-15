from dataclasses import dataclass, field

from framework.com_example_teamcity_api.models.build_type import BuildType
from framework.com_example_teamcity_api.models.project import Project
from framework.com_example_teamcity_api.models.user import User


@dataclass
class TestData:
    project: Project = field(default_factory=Project)
    user: User = field(default_factory=User)
    build_type: BuildType = field(default_factory=BuildType)