
help:
	@echo Crude cross-platform makefile

test:
	@echo Running tests
	@py.exe -m unittest discover

run:
	@echo Running ethParse.py
	@py.exe ethParse.py
