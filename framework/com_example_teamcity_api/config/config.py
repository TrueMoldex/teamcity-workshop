import configparser
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


class Config:
    _instance = None
    _CONFIG_FILE = "config.ini"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.__load_properties(cls._CONFIG_FILE)
        return cls._instance

    def __load_properties(self, filename):
        # Предполагаем, что файл находится в директории resources, расположенной относительно main
        config_path = (
            Path(__file__).resolve().parent.parent.parent / "resources" / filename
        )
        if not config_path.exists():
            raise FileNotFoundError(f"Config file '{filename}' not found!")
        self.properties = configparser.ConfigParser()
        self.properties.read(config_path)

    def get_property(self, section: str, key: str):
        if self.properties.has_option(section, key):
            return self.properties.get(section, key)
        raise KeyError(f"Property '{key}' not found in section '{section}'.")

    @classmethod
    def get_config(cls):
        return cls()
