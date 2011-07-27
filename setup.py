from setuptools import setup, find_packages

setup(
  name = 'git-pull-request',
  version = '0.1',
  packages = find_packages(),

  install_requires = [
  ],

  author = 'Andreas Gohr',
  author_email = 'andi@splitbrain.org',

  entry_points = {
    'console_scripts': [
      'git-pull-request = git.pull_request:main',
    ],
  },
)
