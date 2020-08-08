# pyconfigmanager - a minimal python package
*A simple python config manager to load configuration from external file.*

<br/>

## Description
In projects, it is often required to load configuration from external file (which is not the part of your VCS or codebase). Such configurations could be a database config or secret keys of third party services. Main benefits of loading configuration outside of your codebase : 
  - You can change/configure your app without releasing a build.
  - You can save passwords/secrets safely outside your codebase, so you don't have to push them to your VCS.
 
#### What **pyconfigmanager** does?
- Provides a way to define your configurations in a more readable format by using the power of python syntax. This file will be loaded at runtime to your app as python module.
- It keeps a watch for required config keys and it will raise error if they are not provided.

<br/>

## Installation
*Prerequisites*: Python3+ and pip

`pip install pyconfigmanager`

<br/>

## How to use

1. Create external config file. (**config_app.py**)
   and put your configuration in following manner.
   <br/>
   ```
   class DatabaseConfig:
       
       DATABASE_URL = "127.0.0.1"
       USER = "user"
       PASSWORD = "password"
       DATABASE_NAME = "mydb"
   
   ```
   Save this file. (at /etc/config/myapp/config_app.py)

2. Keep track of two things, your config file path and config file name.
   These are required by **pyconfigmanager**. We will pass them as ENV variable to our package.
   Set ENV variables.
   ```
   export CONFIG_PATH=/etc/config/myapp/
   export CONFIG_FILE_NAME=config_app
   ```
   **NOTE: If you don't specify these environment variables, their default values will be used.**
   <br/>
   Default values : CONFIG_PATH=./ and CONFIG_FILE_NAME=config_development
   
3. Now in your application (preferably somewhere at the entry point of your app). Use in following manner.
   ```
   from pyconfigmanager import ConfigFactory
   
   required_classes_and_keys = [
       #{"class_name": <config_class_name>, "config_keys": [<list_of_config_keys>]}
       {"class_name": "DatabaseConfig", "config_keys": ["DATABASE_URL", "USER", "PASSWORD", "DATABASE_NAME"]}
   ]
   
   config_manager = ConfigFactory.get_config_manager(required_classes_and_keys)
   ```

4. Access your config variables
   ```
   config_manager.get("DATABASE_URL")
   config_manager.get("DATABASE_NAME")
   config_manager.get("USER")
   config_manager.get("PASSWORD")
   ```
   
