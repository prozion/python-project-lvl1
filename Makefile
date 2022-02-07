package-install:
	python -m pip install dist/*.whl

package-uninstall:
	python -m pip uninstall hexlet-code

build:
	poetry build

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games