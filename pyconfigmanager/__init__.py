"""
Author: HassanAzam
Email: hassanazam@live.com
Package Description:
    A simple python config manager
    - Loads python app config from external file (Path of external config file and its name are specified via ENV VARS)
    - Validates required keys
    - Prefer readable format to define configurations in external config file
"""

__version__ = 0.1

# Exposed Classes
from pyconfigmanager.src.config_manager_factory import ConfigFactory
