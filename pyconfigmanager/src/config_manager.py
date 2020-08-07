import sys
import importlib


class ConfigManagerMissingClassException(Exception):
    pass


class ConfigManagerMissingKeyException(Exception):
    pass


class ConfigManager:

    DEVELOPMENT = "development"
    RELEASE = "release"
    MOCKED = "mocked"
    PRODUCTION = "production"

    """
    A manager class to handle and managing app configuration according to ENV variable.
    ENV variable: It is a environment variable which specifies type of environment in which App will be run
    """

    # External config path should be provided, if not then ConfigManager will try to load the file from this path
    DEFAULT_CONFIG_PATH = "./"
    DEFAULT_ENVIRONMENT_NAME = DEVELOPMENT
    DEFAULT_CONFIG_FILE_NAME = "config_development"

    # Config Classes and their required configuration keys
    ###
    # Important
    # Updated this after adding any new config class or config key
    ###

    def __init__(self, config_name, config_path, required_keys):

        """
        Config Manager Initializer
        It takes two environment variables as input: ENV and CONFIG_PATH
        If these are not provided then default values will be used to initialize the App Config
        environment_name: possible values [DEV or PROD or RELEASE]
        config_path: possible values [/etc/config/config_dev]
        :param required_keys: Mapper of required of classes and their config keys
        """

        # Dict field which holds all the app configurations
        self.APP_CONFIG = dict()

        self.CONFIG_FILE_NAME = config_name
        self.CONFIG_PATH = config_path
        self.REQUIRED_KEYS = required_keys

        self.load_app_config()

    def get(self, key):
        """
        Return value of the provided key from APP_CONFIG dict
        :param key:
        :return: value of provided key
        """

        return self.APP_CONFIG[key]

    def load_app_config(self):
        """
        Load config from external path
        :return: None
        """

        # Add config path to system path
        sys.path.insert(0, self.CONFIG_PATH)

        # Load config file
        config = importlib.import_module(self.CONFIG_FILE_NAME)

        # Verify that all required Config classes and their keys exist
        self.process_config(config)

    def process_config(self, config):

        # Load required configs from imported config
        for config_class in self.REQUIRED_KEYS:

            # Validate that config class exist in external config
            if not hasattr(config, config_class["class_name"]):
                raise ConfigManagerMissingClassException

            _class = getattr(config, config_class["class_name"])
            for key in config_class["config_keys"]:
                if not hasattr(_class, key):
                    raise ConfigManagerMissingKeyException("[{}] Key is missing from following class [{}]".format(key,
                        config_class["class_name"]))

                # Add key,value config to the APP_CONFIG
                self.APP_CONFIG[key] = getattr(_class, key)
