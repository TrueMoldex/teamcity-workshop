import requests
import logging
from requests import Response

from framework.com_example_teamcity_api.config.config import Config
from framework.com_example_teamcity_api.models.user import User

logging.basicConfig(level=logging.INFO)

class Specification:
    @staticmethod
    def req_builder():
        session = requests.Session()
        session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        return session

    @staticmethod
    def super_user_auth_spec():
        session = Specification.req_builder()
        superuser_token = Config.get_config().get_property("credentials", "superuser")
        base_uri = f"http://{superuser_token}@{Config.get_config().get_property('server', 'host')}:{Config.get_config().get_property('server', 'port')}"
        session.auth = ("", superuser_token)

        return session, base_uri  # Теперь в base_uri есть суперпользователь
    @staticmethod
    def unauth_spec():
        return Specification.req_builder()

    @staticmethod
    def auth_spec(user: User):
        session = Specification.req_builder()
        base_uri = f"http://{user.username}:{user.password}@{Config.get_config().get_property('server', 'host')}:{Config.get_config().get_property('server', 'port')}"
        session.auth = (user.username, user.password)
        return session, base_uri
