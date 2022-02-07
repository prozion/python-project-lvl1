install:
	python -m pip install --force-reinstall dist/*.whl

uninstall:
	python -m pip uninstall hexlet-code

setup:
	poetry install

lint: lint-flake8

lint-flake8:
	poetry run flake8 brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games