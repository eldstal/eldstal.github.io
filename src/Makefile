DEST=..
STATICS=$(patsubst static/%,$(DEST)/%,$(wildcard static/*))
PAGES=$(addprefix $(DEST)/,$(patsubst %.md,%.html,$(wildcard *.md */*.md)))


all: $(PAGES) $(STATICS)

$(DEST)/%.html: %.md header.html template.html Makefile
	mkdir -p $$(dirname $@)
	# Preprocessor from http://christophe.delord.free.fr/upp/
	upp $< > /tmp/preproc.md
	pandoc -M date="$$(date '+%B %e, %Y')" -f markdown -t html5 --template `dirname $<`/template.html -H `dirname $<`/header.html -o $@ /tmp/preproc.md


cve.md: tools/gen_cve.py cve.json
	tools/gen_cve.py cve.json > $@

$(DEST)/%: static/%
	cp $< $@
	chmod 644 $@

