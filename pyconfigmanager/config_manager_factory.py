import os

from pyconfigmanager.config_manager import ConfigManager


class ConfigFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_config_manager(required_keys):

        """
        Initialize ConfigManager with the following paramteres
        - ENV: name of environment in which app will run. LIKE [development, production etc]
        - CONFIG_PATH: path of external config file (Default: root directory of project)
        - CONFIG_FILE_NAME: name of the config file

        :return: ConfigManager object to load config values from external file (outside codebase)
        """

        config_name = os.environ.get("CONFIG_FILE_NAME", ConfigManager.DEFAULT_CONFIG_FILE_NAME)
        config_path = os.environ.get("CONFIG_PATH", ConfigManager.DEFAULT_CONFIG_PATH)
        config_manager = ConfigManager(config_name, config_path, required_keys)

        return config_manager
