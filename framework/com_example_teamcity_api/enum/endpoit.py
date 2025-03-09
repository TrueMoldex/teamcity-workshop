from enum import Enum
from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.models.build_type import BuildType


class Endpoint(Enum):

    BUILD_TYPES = ("/app/rest/buildTypes", BuildType)

    def __init__(self, url: str, model_class: type[BaseModel]):
        self.url = url
        self.model_class = model_class