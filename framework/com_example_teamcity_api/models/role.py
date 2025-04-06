from framework.com_example_teamcity_api.models.base_model import BaseModelPD


class Role(BaseModelPD):
    roleId: str = "SYSTEM_ADMIN"
    scope: str = "g"