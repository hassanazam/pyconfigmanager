from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
  name = 'pyconfigmanager',
  packages = ['pyconfigmanager'],
  version = 'v0.2.4-alpha',
  license='MIT',
  description = 'A simple config manager to load configuration file from outside of project',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'MHA',
  author_email = 'hassanazam@live.com',
  url = 'https://github.com/hassanazam/pyconfigmanager',
  download_url = 'https://github.com/HassanAzam/pyconfigmanager/archive/v0.2.4-alpha.tar.gz',
  keywords = ['python config manager', 'config management', 'python config'],
  install_requires=[
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
