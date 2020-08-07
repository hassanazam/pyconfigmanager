from setuptools import setup

setup(
  name = 'pyconfigmanager',
  packages = ['pyconfigmanager'],
  version = '0.1',
  license='MIT',
  description = 'A simple config manager to load configuration file from outside of project',
  author = 'MHA',
  author_email = 'hassanazam@live.com',
  url = 'https://github.com/hassanazam/pyconfigmanager',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['python config manager', 'config management', 'python config'],
  install_requires=[
          'validators',
          'beautifulsoup4',
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