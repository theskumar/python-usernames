.PHONY: clean-pyc clean-build

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

release: clean sdist
	twine check dist/*
	twine upload dist/*

release-test: sdist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

sdist: clean
	python setup.py sdist bdist_wheel
	ls -l dist
