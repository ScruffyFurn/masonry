# Running pytest unit tests

As part of the workflow solution and development container, the [pytest](https://docs.pytest.org/en/7.0.x/)
unit testing and [Bandit](https://bandit.readthedocs.io/en/latest/) security testing frameworks have been
installed and configured.

To make running the unit and security tests a little easier, a "make test" step, in the projects [MakeFile](../src/Makefile) has been provided.

The MakeFile test step will call any pytest(s) located in the __src/tests/__ directory. The pytest call will also generate a __test-results.xml__ juintxml file. The test step will also call Bandit to run security checks against any python files located in the library's source files (src/example_library in the examples' case). The Bandit call will also generate a __security.xml__ junit style result file.

MakeFile test step:

```MakeFile
test: dev
   pytest --ignore=sandbox --doctest-modules --junitxml=junit/test-results.xml
   bandit -r ./example_library/*.py -f xml -o junit/security.xml || true
```

## Running Tests

To run the unit and security tests, from the terminal, we use the make test command.

In the Terminal, from the __src__ directory:

```bash
make test
```
