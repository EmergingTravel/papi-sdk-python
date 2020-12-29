pip:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
	poetry install

clean:
	find . -name '*.pyc' | xargs rm -rf
	find . -name '*__pycache__' | xargs rm -rf
	find . -name '*.cache' | xargs rm -rf

autoflake:
	autoflake -i -r papi_sdk

isort:
	isort -rc papi_sdk

black:
	black papi_sdk

lint: clean autoflake isort black

test:
	python -m unittest discover

install_tox:
	pip install tox poetry

tox: install_tox
	tox -e $(VERSION)
