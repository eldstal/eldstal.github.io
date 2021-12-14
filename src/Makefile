DEST=..
STATICS=$(patsubst static/%,$(DEST)/%,$(wildcard static/*))
PAGES=$(addprefix $(DEST)/,$(patsubst %.md,%.html,$(wildcard *.md)))


all: $(PAGES) $(STATICS)

$(DEST)/%.html: %.md header.html template.html Makefile
	mkdir -p $(DEST)
	#pandoc --self-contained -M date="$$(date '+%B %e, %Y')" -f markdown -t html5 --template template.html -H header.html -o $@ $<
	pandoc -M date="$$(date '+%B %e, %Y')" -f markdown -t html5 --template template.html -H header.html -o $@ $<

$(DEST)/%: static/%
	cp $< $@
	chmod 644 $@

