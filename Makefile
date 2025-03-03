all:
	pelican src/

dev:
	pelican -l --relative-urls --autoreload src/
