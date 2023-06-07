PROJECT_NAME=chat_api

.PHONY: install
install:
	pip3 install --quiet --upgrade pip
	pip3 install --quiet -r requirements.txt -r requirements-dev.txt

.PHONY: dev
dev:
	HOST=localhost PORT=8080 python3 -m chat_api

.PHONY: check-types
check-types:
	python3 -m mypy ${PROJECT_NAME} --strict

.PHONY: check-imports
check-imports:
	python3 -m isort ${PROJECT_NAME} tests --check-only

.PHONY: sort-imports
sort-imports:
	python3 -m isort ${PROJECT_NAME} tests

.PHONY: check-style
check-style:
	python3 -m flake8 ${PROJECT_NAME} tests

.PHONY: lint
lint: check-types check-style check-imports

.PHONY: test
test:
	cd tests/ && API_URL=http://localhost:8080/tl3mzuetbb vedro run
