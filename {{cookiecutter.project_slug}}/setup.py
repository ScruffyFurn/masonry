"""Setup.py script for packaging project."""
from setuptools import setup
import os
setup(
    name='{{cookiecutter.project_slug}}',
    packages=["{{cookiecutter.project_slug}}"],
    version=os.getenv('PACKAGE_VERSION', '0.0.dev0'),
    description='{{cookiecutter.project_short_description}}',
    author='{{cookiecutter.author_name}}',
    license_files = ('../LICENSE'),
    install_requires=[]
)
