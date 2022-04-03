install:
	python install -r requirements.txt
setup:
	python setup.py install
lint:
	pylint * --ignore build dist
lint-fix:
	autopep8 --in-place --aggressive --aggressive *.py