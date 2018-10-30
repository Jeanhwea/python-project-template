PYTHON := python
PIP    := pip

all: test

init:
	$(PIP) install -r requirements.txt

test:
	$(PYTHON) -m unittest

browse:
	grip -b

.PHONY: init test
