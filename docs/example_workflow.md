# An example workflow

The masonry framework can be thought of in three (3) different components;
The Dev Container, the CLI,  and the CI/CD pipelines.

The Dev Container provides the development environment for building complete Databricks solutions with full testing on remote clusters included.

The CLI provides a simple interface for creating, testing, and linting of python libraries and Databricks notebooks.

The CI/CD pipelines provide the final component of the masonry framework, it provides a solution for publishing libraries and notebooks using Devops patterns and principles.

## Full workflow

Below is an flow diagram demonstrating the flow of development when using the masonry framework:
![Full workflow](images/workflow.svg)

## Azure DataBricks Notebook/Library usage

The main design pattern implemented in the masonry framework is the idea of business logic python libraries being called from a orchestrator Databrick notebook.

Below is a simple diagram explaining this concept:
![Notebook](images/databricks.svg)
