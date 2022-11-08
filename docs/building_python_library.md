# Building a Python library

To make the building and ultimately the deployment of a DataBricks Python library easier,
a [MakeFile](../src/Makefile) with all the necessary build steps has been provided.

The MakeFile first calls the __clean__ Make step first to clean up any previous builds, installs wheel, finally builds the library using the packaging information in the [setup.py](../src/setup.py) file.

MakeFile build step:

```MakeFile
build: clean
    pip install wheel
    python setup.py bdist_wheel
```

## Build steps

Before we can call the MakeFiles' build step, we must first provide a little information about our library that is being packaged. To do this we create a "setup" file in the head of the src directory.

The __setup.py__ file defines the information about the library. It contains a name, version, description, as well as any external requirements, and the definition of any method to be exported.

Example library's __setup.py__ file:

```python
"""Setup.py script for packaging project."""
from setuptools import setup, find_packages
import os

if __name__ == '__main__':
    setup(
        name='example_library',
        version=os.getenv('PACKAGE_VERSION', '0.0.dev0'),
        package_dir={'': 'example_library'},
        packages=find_packages('example_library', include=[
            'game_name_check*'
        ]),
        description='Example Library.',
        install_requires=[
        ]
    )
```

Once we have populated the setup file we can build our library with one command.

From the terminal, in the src directory, type the following:

```bash
make build
```

Once completed a packaged version of the library can be found in the __src/dist__ directory.
