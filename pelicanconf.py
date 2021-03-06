#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import os.path
import sys

import markupsafe


def social(fa, title, url):
    markup = f'<i class="fa fa-{fa}" aria-hidden="true" title="{title}"></i>'
    return (markupsafe.Markup(markup), url)


AUTHOR = "Keith Gaughan"
SITENAME = AUTHOR
TAGLINE = "An attempt at public introspection"
SITEURL = "/"

SLUGIFY_SOURCE = "basename"

PATH = "content"

TIMEZONE = "Europe/Dublin"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None

# fmt: off
DEFAULT_METADATA = {
    "status": "draft",
}

LINKS = [
    ("Inklings", "https://talideon.com/inklings/"),
]

SOCIAL = [
    social(
        "stack-overflow",
        "Stack Overflow",
        "https://stackoverflow.com/users/8342/keith-gaughan",
    ),
    social("linkedin", "LinkedIn", "https://www.linkedin.com/in/keithgaughan"),
    social("github", "Github", "https://github.com/kgaughan/"),
]
# fmt: on

PLUGIN_PATHS = [os.path.abspath("../pelican-plugins")]
sys.path += PLUGIN_PATHS
PLUGINS = [
    # https://github.com/getpelican/pelican-plugins/tree/master/code_include
    "code_include",
    # https://github.com/getpelican/pelican-plugins/tree/master/more_categories
    "more_categories",
    # https://github.com/akhayyat/pelican-page-hierarchy/
    "pelican-page-hierarchy",
    # https://github.com/getpelican/pelican-plugins/tree/master/readtime
    "readtime",
    # https://github.com/getpelican/pelican-plugins/tree/master/series
    "series",
    # https://github.com/getpelican/pelican-plugins/tree/master/sitemap
    "sitemap",
]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.attr_list": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.admonition": {},
    },
    "output_format": "html5",
}

DOCUTILS_SETTINGS = {
    "restructuredtext parser": {"smart_quotes": True},
    "html5 writer": {"table_style": "colwidths-auto"},
}

# fmt: off
STATIC_PATHS = [
    "images",
    "extra/robots.txt",
    "extra/favicon.ico",
]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}
# fmt: on

THEME = os.path.join(os.curdir, "themes", "air-and-fire")

SITEMAP = {"format": "xml"}

DEFAULT_PAGINATION = 20

# Pages to disable.
ARCHIVES_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""

ARTICLE_PATHS = ["blog"]
PAGE_PATHS = ["pages"]

DEFAULT_DATE_FORMAT = "%d %B %Y"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
CATEGORIES_URL = "categories/"
CATEGORIES_SAVE_AS = "categories/index.html"
CATEGORY_URL = "categories/{slug}/"
CATEGORY_SAVE_AS = "categories/{slug}/index.html"

TYPOGRIFY = True
