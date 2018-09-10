#!/usr/local/bin/python3.6

import cgitb
import json
import markdown
import mimetypes
import os
import re
import magic
from markdown.extensions.toc import TocExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from urllib.parse import parse_qs
from pygments import highlight
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.formatters import HtmlFormatter

# cgitb.enable()
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

settings_file = open(os.path.join(__location__, 'config.json'))
SETTINGS = json.loads(settings_file.read())

ALWAYS_ACTIVE = SETTINGS['ExtensionsActiveByDefault']
FORMAT_QUERY = SETTINGS['URL_FormatKey']
THEME_QUERY = SETTINGS['URL_ThemeKey']
THEMES = SETTINGS['AvailableThemes']
EXTENSIONS = [
    'subscript',
    'superscript',
    'markdown_checklist.extension',
    'markdown.extensions.extra',
    'markdown.extensions.admonition',
    'markdown.extensions.meta',
    'markdown.extensions.nl2br',
    TocExtension(
        title="Contents:",
        anchorlink=True
    ),
    CodeHiliteExtension(
        linenums=False
    )
]
DIRNAME, FULL_FILE_NAME = os.path.split(os.environ['PATH_TRANSLATED'])
FILENAME, FILE_EXTENSION = os.path.splitext(os.environ['PATH_TRANSLATED'])
URL_QUERY = parse_qs(os.environ['QUERY_STRING'])
Heading = FULL_FILE_NAME
DOC = []
f = open(FILENAME + FILE_EXTENSION, 'r')


def FormatFile(text, extension):
    InnerHTML = None
    if (extension == ".md"):
        InnerHTML = markdown.markdown(
            text=text, output_format="html5", extensions=EXTENSIONS).splitlines()
    else:
        code = text
        lexer = guess_lexer_for_filename(FULL_FILE_NAME, code)
        formatter = HtmlFormatter(linenos=False, cssclass="codehilite")
        result = highlight(code, lexer, formatter)
        InnerHTML = [result]
    return InnerHTML


FileOutput = f.read()
if ((FORMAT_QUERY not in URL_QUERY and FILE_EXTENSION not in ALWAYS_ACTIVE) or (FORMAT_QUERY in URL_QUERY and URL_QUERY[FORMAT_QUERY][0].lower() not in [1, "1", "yes", "y"])):
    m = magic.Magic(mime=True)
    mime = (m.from_file(FILENAME + FILE_EXTENSION), None)
    if (mime[0] == None):
        mime = ("text/plain", None)
    print("Content-type: " + mime[0] + ";charset=UTF-8\r\n\r\n")
    print(FileOutput)
else:
    InnerHTML = FormatFile(FileOutput, FILE_EXTENSION)
    if (THEME_QUERY in URL_QUERY):
        theme = URL_QUERY[THEME_QUERY][0].upper()
        if (theme in THEMES):
            stylesheet = THEMES[theme]['Stylesheet']
        else:
            stylesheet = THEMES[SETTINGS['DefaultTheme']]['Stylesheet']
    else:
        stylesheet = THEMES[SETTINGS['DefaultTheme']]['Stylesheet']

    DOC.append("<!DOCTYPE html>")
    DOC.append("<html>")
    DOC.append("<head>")
    DOC.append("<title>" + Heading + "</title>")
    DOC.append(
        '<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">')
    # DOC.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    # DOC.append('<link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i&amp;subset=latin-ext" rel="stylesheet">')
    DOC.append('<link rel="stylesheet" href="/CH/CSS/' + stylesheet + '">')
    DOC.append("</head>")
    DOC.append("<body>")
    DOC.append("<div id='Wrapper'>")
    DOC.extend(InnerHTML)
    DOC.append("</div>")
    DOC.append("</body>")
    DOC.append("</html>")

    DOC = '\n'.join(DOC)
    print("Content-type: text/html;charset=UTF-8\r\n\r\n")
    print(DOC)
