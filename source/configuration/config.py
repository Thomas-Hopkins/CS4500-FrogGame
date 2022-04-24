import os
import json


class Config:

    __instance = None
    __DATA = None
    __VERSION = "0.1"
    __CONFIG_FILE = "../config.json"

    def __init__(self):
        if Config.__instance:
            raise Exception(
                "Cannot instantiate a singleton with an instance already created!"
            )
        else:
            Config.__DATA = {"language": "en", "num_frogs": 6, "theme": "light"}
            Config.load_config()

            Config.__instance = self

    @staticmethod
    def get_instance():
        if Config.__instance:
            return Config.__instance
        else:
            return Config()

    @staticmethod
    def load_config():
        if not os.path.exists(Config.__CONFIG_FILE):
            Config.save_config()
            # No need to load data from config since we just saved current default data
            return

        with open(Config.__CONFIG_FILE, "rt") as config_file:
            Config.__DATA = json.load(config_file)

    @staticmethod
    def save_config():
        with open(Config.__CONFIG_FILE, "wt") as config_file:
            json.dump(Config.__DATA, config_file)

    @staticmethod
    def get(attr: str):
        if attr == "version":
            return Config.__VERSION
        else:
            # Improvement: Verify this data before returning it. Currently malformed data could cause a crash.
            return Config.__DATA.get(attr)

    @staticmethod
    def set(attr: str, value):
        curr_value = Config.__DATA.get(attr)
        if not curr_value:
            raise Exception(f"Config for {attr} does not exist!")

        if not isinstance(value, type(curr_value)):
            raise Exception(
                f"Config value {value} for {attr} does not match type {type(curr_value)}"
            )

        Config.__DATA[attr] = value
