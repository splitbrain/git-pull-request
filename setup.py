from setuptools import setup, find_packages

setup(
  name = 'git-pull-request',
  version = '0.1',
  packages = find_packages(),

  install_requires = [
  ],

  author = 'Andreas Gohr',
  author_email = 'andi@splitbrain.org',

  scripts = [
    'git-pull-request',
  ],
)
