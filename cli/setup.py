from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name="masonry",
    version="0.0.2",
    author="Mickey MacDonald ",
    author_email="Mickey MacDonald",
    license="MIT",
    description="A cli tool for creating and working with DataBrick Python \
         libraries and notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/scruffyfurn/masonry/",
    py_modules=["masonry", "app"],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        masonry=masonry:cli
    """,
)
