all: test

init:
	pip3 install -r requirements.txt

test:
	python3 -m unittest

preview:
	grip -b

.PHONY: init test
