SVG=$(wildcard *.svg)
PNG=$(patsubst %.svg,%.png,$(SVG))

all: $(PNG)

%.png: %.svg
	inkscape --export-dpi=96 --export-png=$@ $<
