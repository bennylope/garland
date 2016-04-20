.PHONY: clean-pyc clean-build docs clean

clean: clean-build clean-pyc clean-test  ## remove all build, test, coverage and Python artifacts

clean-build:  ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:  ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:  ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:  ## check style with flake8
	flake8 garland tests

test:  ## run tests quickly with the default Python
	python setup.py test

test-all:  ## run tests on every Python version with tox
	tox

coverage:  ## check code coverage quickly with the default Python
	coverage run --source garland setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:  ## generate Sphinx HTML documentation, including API docs
	rm -f docs/garland.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ garland
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

release: clean  ## package and upload a release
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean  ## create packages
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

help:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
