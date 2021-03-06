COURSE_NAME = '2019-CS109B'

AUTHOR = 'Pavlos Protopapas'

SITEURL = 'https://harvard-iacs.github.io/2019-CS109B/'

GITHUB = 'https://github.com/Harvard-IACS/2019-CS109B'

COLOR = '#A51C30'

MENUITEMS = []

PATH = 'content'

OUTPUT_PATH = 'docs'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None

CATEGORY_FEED_ATOM = None

TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM = None

AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = 'pages'

AUTHORS_SAVE_AS = ''

CATEGORIES_SAVE_AS = ''

ARCHIVES_SAVE_AS = ''

ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

ARTICLE_URL = '{category}/{slug}/'

AUTHOR_URL = ''

AUTHOR_SAVE_AS = ''

INDEX_SAVE_AS = 'pages/materials.html'

THEME_STATIC_DIR = 'style'

DELETE_OUTPUT_DIRECTORY = True

MARKUP = ['md', 'ipynb']

PLUGIN_PATHS = ['plugins']

PLUGINS = ['ipynb.markup', 'tipue_search']

IGNORE_FILES = ['.ipynb_checkpoints']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['lectures', 'labs', 'homeworks', 'sections', 'wiki', 'images', 'projects']

DIRECT_TEMPLATES = ['index', 'category', 'tags', 'search']

import re

JINJA_FILTERS = {
    'original_content': lambda x: re.search(r"content/.*", x).group(0)
}

USE_FOLDER_AS_CATEGORY = False

IGNORE_FILES = ['README.md']
