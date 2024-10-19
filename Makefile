install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/hexlet_code-0.1.0-py3-none-any.whl

gendiff:
	poetry run gendiff

generate_diff:
	poetry run generate_diff
