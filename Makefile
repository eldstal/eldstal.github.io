CSS:=pelican-theme/static/css
MD_INCLUDE:=src/md-include

all: gen
	pelican src/
	cp CNAME docs/CNAME

dev: gen
	pelican -l --relative-urls --autoreload src/

gen: $(MD_INCLUDE)/cve.md $(CSS)/eldstal-colors.css

$(MD_INCLUDE)/cve.md: $(MD_INCLUDE)/cve.json tools/gen_cve.py
	./tools/gen_cve.py "$<" > "$@"

$(CSS)/eldstal-colors.css: tools/colors.py
	./tools/colors.py > "$@"
