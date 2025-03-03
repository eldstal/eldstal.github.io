all:
	pelican src/
	cp CNAME docs/CNAME

dev:
	pelican -l --relative-urls --autoreload src/
