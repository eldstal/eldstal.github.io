all: src/md-include/cve.md
	pelican src/
	cp CNAME docs/CNAME

dev: src/md-include/cve.md
	pelican -l --relative-urls --autoreload src/

src/md-include/cve.md: src/md-include/cve.json tools/gen_cve.py
	./tools/gen_cve.py "$<" > "$@"
