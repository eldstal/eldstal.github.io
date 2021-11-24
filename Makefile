STATICS=$(patsubst static/%,site/%,$(wildcard static/*))
PAGES=$(addprefix site/,$(patsubst %.md,%.html,$(wildcard *.md)))


all: $(PAGES) $(STATICS)

site/%.html: %.md header.html template.html Makefile
	mkdir -p site
	#pandoc --self-contained -M date="$$(date '+%B %e, %Y')" -f markdown -t html5 --template template.html -H header.html -o $@ $<
	pandoc -M date="$$(date '+%B %e, %Y')" -f markdown -t html5 --template template.html -H header.html -o $@ $<

site/%: static/%
	cp $< $@
	chmod 644 $@

