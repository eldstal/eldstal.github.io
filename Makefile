STATICS=$(patsubst static/%,site/%,$(wildcard static/*))


all: site/index.html $(STATICS)

site/index.html: index.md header.html metadata.yaml Makefile
	mkdir -p site
	pandoc --self-contained -f markdown -t html5 -H header.html -o $@ $< metadata.yaml

site/%: static/%
	cp $< $@
	chmod 644 $@
