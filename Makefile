STATICS=$(patsubst static/%,docs/%,$(wildcard static/*))
PAGES=$(addprefix docs/,$(patsubst %.md,%.html,$(wildcard *.md)))


all: $(PAGES) $(STATICS)

docs/%.html: %.md header.html template.html Makefile
	mkdir -p docs
	#pandoc --self-contained -M date="$$(date '+%B %e, %Y')" -f markdown -t html5 --template template.html -H header.html -o $@ $<
	pandoc -M date="$$(date '+%B %e, %Y')" -f markdown -t html5 --template template.html -H header.html -o $@ $<

docs/%: static/%
	cp $< $@
	chmod 644 $@

