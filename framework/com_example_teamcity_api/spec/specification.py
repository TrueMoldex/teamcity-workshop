import requests
import logging
from requests import Response

from framework.com_example_teamcity_api.config.config import Config
from framework.com_example_teamcity_api.models.user import User

logging.basicConfig(level=logging.INFO)

class Specification:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__init_spec()
        return cls._instance

    def __init_spec(self):
        config = Config.get_config()
        self.host = config.get_property("server", "host")
        self.port = config.get_property("server", "port")
        self.default_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        # Можно создать одну сессию, если хотим переиспользовать (куки, коннекты и т.д.)
        self.session = requests.Session()
        self.session.headers.update(self.default_headers)

    def __req_builder(self):
        return {
            "base_uri": f"http://{self.host}:{self.port}",
            "headers": self.default_headers,
        }

    def unauth_spec_request(self, endpoint: str, method: str = "GET", **kwargs) -> Response:
        """
        Запрос без аутентификации, только базовый URL (host:port).
        """
        builder = self.__req_builder()
        url = f"{builder['base_uri']}{endpoint}"
        logging.info(f"Sending {method} request to {url} (unauth)")
        response = self.session.request(method, url, headers=builder["headers"], **kwargs)
        logging.info(f"Response: {response.status_code} {response.text}")
        return response

    def auth_spec_request(self, user: User, endpoint: str, method: str = "GET", **kwargs) -> Response:
        """
        Запрос с аутентификацией через URL: http://user:password@host:port.
        """
        builder = self.__req_builder()
        url = f"{builder['base_uri']}{endpoint}"
        logging.info(f"Sending {method} request to {url} (auth)")
        response = self.session.request(
            method,
            url,
            headers=builder["headers"],
            auth=(user.user, user.password),
            **kwargs)
        logging.info(f"Response: {response.status_code} {response.text}")
        return response