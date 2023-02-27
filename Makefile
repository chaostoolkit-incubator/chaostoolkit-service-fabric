.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: install-dev
install-dev: install
	pip install -r requirements-dev.txt
	python setup.py develop

.PHONY: lint
lint:
	flake8 --ignore=E251 chaosservicefabric/ tests/
	isort --check-only --profile black chaosservicefabric/ tests/
	black --check --line-length=80 --diff chaosservicefabric/ tests/

.PHONY: format
format:
	isort --profile black chaosservicefabric/ tests/
	black --line-length=80 chaosservicefabric/ tests/

.PHONY: tests
tests:
	pytest
