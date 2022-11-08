"""Setup.py script for packaging project."""
from setuptools import setup
import os
setup(
    name='example_library',
    packages=["example_library"],
    version=os.getenv('PACKAGE_VERSION', '0.0.dev0'),
    description='Example Library',
    author='Microsoft',
    license_files = ('../LICENSE'),
    install_requires=[]
)
