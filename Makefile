STATICS=$(patsubst static/%,site/%,$(wildcard static/*))
PAGES=$(addprefix site/,$(patsubst %.md,%.html,$(wildcard *.md)))


all: $(PAGES) $(STATICS)

site/%.html: %.md header.html Makefile
	mkdir -p site
	pandoc --self-contained -f markdown -t html5 -H header.html -o $@ $<

site/%: static/%
	cp $< $@
	chmod 644 $@
