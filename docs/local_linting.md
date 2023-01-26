# Linting the codebase locally

In order to run the Super-Linter linter locally, you will need to have
Docker or Docker Desktop installed. This document covers the steps to install Docker / Docker Desktop
and run the provided scripts to lint the full code base.

## Run the linting script

Once Docker has been installed, you can lint the entire code base with one command:

### Windows

From the __"scripts"__ project directory

```bash
Lint.bat
```

### Linux/macOS

Before you run the script, you may need to set the permissions for the file.
To do this run the following command.

From the __"scripts"__ project directory

```bash
chmod 755 Lint.sh
```

To run the Linter, use the following command:

From the __"scripts"__ project directory

```bash
./Lint.sh
```

Optionally, when using the Lint.sh script, you can specify the project parent directory by passing in the full path as the first argument of the script. For example:

```bash
./Lint.sh /usr/local/
```
