from framework.com_example_teamcity_api.models.base_model import BaseModelPD


class Build(BaseModelPD):
    state: str
    status: str
    id: str = ""