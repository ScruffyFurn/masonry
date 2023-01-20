help:
	@echo "Tasks in \033[1;32mdata_pipeline\033[0m:"
	@cat Makefile

lint:
	isort ./masonry
	black ./masonry
	mypy ./masonry --ignore-missing-imports
	flake8 ./masonry --ignore=$(shell cat .flakeignore)

dev:
	pip install -e .

test: dev
	pytest --ignore=sandbox --doctest-modules --junitxml=junit/test-results.xml
	bandit -r ./masonry/*.py -f xml -o junit/security.xml || true

build: clean
	pip install wheel
	python setup.py bdist_wheel

clean:
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/ dist/
	@find . -not -path './.venv*' -path '*/__pycache__*' -delete
	@find . -not -path './.venv*' -path '*/*.egg-info*' -delete
