.PHONY: install, lint-format, lint-style, test, test-all

install:
	poetry install

lint-format:
	poetry run black tests

lint-style:
	poetry run pycodestyle tests --show-source

test:
	poetry run pytest

test-all: lint-format lint-style test
