help:
	@echo "Tasks in \033[1;32mdata_pipeline\033[0m:"
	@cat Makefile

lint:
	isort ./example_library
	black ./example_library
	mypy ./example_library --ignore-missing-imports
	flake8 ./example_library --ignore=$(shell cat .flakeignore)

dev:
	pip install -e .

test: dev
	pytest --ignore=sandbox --doctest-modules --junitxml=junit/test-results.xml
	bandit -r ./example_library/*.py -f xml -o junit/security.xml || true

build: clean
	pip install wheel
	python setup.py bdist_wheel

clean:
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/ dist/
	@find . -not -path './.venv*' -path '*/__pycache__*' -delete
	@find . -not -path './.venv*' -path '*/*.egg-info*' -delete
