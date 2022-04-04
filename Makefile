install:
	pip3 install -r requirements.txt
setup:
	python3 setup.py install
lint:
	pylint * --ignore build dist
lint-fix:
	autopep8 --in-place --aggressive --aggressive *.py