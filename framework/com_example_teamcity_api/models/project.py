from typing import Optional

from framework.com_example_teamcity_api.models.base_model import BaseModelPD


class ParentProjectLocator(BaseModelPD):
    id: str


class Project(BaseModelPD):
    id: str = ""
    name: str = ""
    parentProjectLocator: Optional[ParentProjectLocator] = None
