from attr import dataclass

from framework.com_example_teamcity_api.models.build_type import BuildType
from framework.com_example_teamcity_api.models.project import Project
from framework.com_example_teamcity_api.models.user import User


@dataclass
class TestData:
    project: Project = None
    user: User = None
    build_type: BuildType = None