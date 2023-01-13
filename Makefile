# /////////////////////////////////////////////////////////////////////////////////////////////////
# MAKEFILE FOR TRADING PROJECT
# /////////////////////////////////////////////////////////////////////////////////////////////////
.PHONY: help create-venv clean clean-build clean-pyc clean-cov test install-lint update-lint lint

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  create-venv                to make python virtual environment"
	@echo "  clean                      to clean build, test, coverage and python artifacts"
	@echo "  clean-build                to clean python build artifacts"
	@echo "  clean-pyc                  to clean python file artifacts"
	@echo "  clean-cov                  to clean python test and coverage artifacts"
	@echo "  test                       to run unit tests"
	@echo "  install-lint               to install python linting tools / git hooks"
	@echo "  update-lint                to update python linting tools / git hooks"
	@echo "  lint                       to run autopep8, flake, black and other linting tools"
	@echo "  run                        to run the main application"

PYTHON = python
VENV_DIR = .venv
MAIN_APP = trading

# Create python virtual environment
create-venv:
	$(PYTHON) -m venv $(VENV_DIR)
	source $(VENV_DIR)/bin/activate \
	&& pip install -r $(MAIN_APP)/requirements.txt \
	&& pip install -r $(MAIN_APP)/requirements-dev.txt \
	&& pip install -r tests/requirements.txt

# Remove all build, test, coverage and python artifacts.
clean: clean-build clean-pyc clean-cov

# Remove Python build artifacts
clean-build:
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

# Remove Python file artifacts
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

# Remove pytest and coverage files
clean-cov:
	find . -name '.pytest_cache' -exec rm -rf {} +
	find . -name '.coverage' -exec rm -rf {} +
	find . -name 'coverage_html_report' -exec rm -rf {} +

# Uses pyproject.toml for configs
test: clean-pyc clean-cov
	$(PYTHON) -m pytest

install-lint:
	pip install pre-commit
	pre-commit install

update-lint:
	pre-commit autoupdate

lint:
	pre-commit run -a

run:
	$(PYTHON) $(MAIN_APP)/main.py
