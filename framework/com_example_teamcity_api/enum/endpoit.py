from enum import Enum

from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.models.build import Build
from framework.com_example_teamcity_api.models.build_type import BuildType
from framework.com_example_teamcity_api.models.project import Project
from framework.com_example_teamcity_api.models.user import User


class Endpoint(Enum):

    BUILD_TYPES = ("/app/rest/buildTypes", BuildType)
    PROJECTS = ("/app/rest/projects", Project)
    USERS = ("/app/rest/users", User)
    BUILD_QUEUE = ("/app/rest/buildQueue", Build)

    def __init__(self, url: str, model_class: type[BaseModel]):
        self.url = url
        self.model_class = model_class
