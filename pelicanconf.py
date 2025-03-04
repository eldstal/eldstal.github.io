SITENAME = "Albin Eldstål-Ahrens"
SITEURL = "https://eldstal.se"
TIMEZONE = "Europe/Stockholm"
AUTHOR = "Albin Eldstål-Ahrens"

PLUGINS = [ "md_include" ]
MD_INCLUDE_BASE_PATH = "src/md-include"

MARKDOWN = {
        "extension_configs": {
            "markdown.extensions.md_in_html": {},
            "markdown.extensions.extra": {},
            "markdown.extensions.meta": {},
            "markdown.extensions.codehilite": {"css_class": "highlight"},
        }

}

PATH = 'src'
OUTPUT_PATH = 'docs/'
THEME = 'pelican-theme'

ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'

PAGE_PATHS = [ 'pages', 'advisories' ]
PAGE_URL = '{slug}.html'
DISPLAY_PAGES_ON_MENU = False

# Don't need these pages
AUTHOR_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
