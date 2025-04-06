from framework.com_example_teamcity_api.models.base_model import BaseModelPD


class Step(BaseModelPD):
    id: str = ""
    name: str = ""
    type: str = "simpleRunner"
