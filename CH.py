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

try:
    settings_file = open(os.path.join(__location__, 'config.json'))
except FileNotFoundError:
    SETTINGS = {
        "DefaultTheme": "DARK",
        "ExtensionsActiveByDefault": [".md", ".txt", ".sql", ".java", ".cs", ".py"],
        "URL_FormatKey": "CH_FORMAT",
        "URL_ThemeKey": "CH_THEME",
        "AvailableThemes": {
            "DARK": {
                "Stylesheet": "DARK.min.css"
            },
            "LIGHT": {
                "Stylesheet": "LIGHT.min.css"
            }
        }
    }
else:
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
    DOC.append(
        "<link rel='shortcut icon' href='/CH/favicon.ico' type='image/x-icon'>")
    DOC.append(
        "<link rel='apple-touch-icon' href='/CH/Icons/apple-icon-57x57.png' sizes='57x57'>")
    DOC.append(
        "<link rel='apple-touch-icon' href='/CH/Icons/apple-icon-60x60.png' sizes='60x60'>")
    DOC.append(
        "<link rel='apple-touch-icon' href='/CH/Icons/apple-icon-72x72.png' sizes='72x72'>")
    DOC.append(
        "<link rel='apple-touch-icon' href='/CH/Icons/apple-icon-76x76.png' sizes='76x76'>")
    DOC.append(
        "<link rel='apple-touch-icon' href='/CH/Icons/apple-icon-114x114.png' sizes='114x114'>")
    DOC.append(
        "<link rel='apple-touch-icon' href='/CH/Icons/apple-icon-120x120.png' sizes='120x120'>")
    DOC.append(
        "<link rel='apple-touch-icon' href='/CH/Icons/apple-icon-144x144.png' sizes='144x144'>")
    DOC.append(
        "<link rel='apple-touch-icon' href='/CH/Icons/apple-icon-152x152.png' sizes='152x152'>")
    DOC.append(
        "<link rel='apple-touch-icon' href='/CH/Icons/apple-icon-180x180.png' sizes='180x180'>")
    DOC.append(
        "<link rel='icon' href='/CH/Icons/android-icon-192x192.png' type='image/png' sizes='192x192'>")
    DOC.append(
        "<link rel='icon' href='/CH/Icons/favicon-32x32.png' type='image/png' sizes='32x32'>")
    DOC.append(
        "<link rel='icon' href='/CH/Icons/favicon-96x96.png' type='image/png' sizes='96x96'>")
    DOC.append(
        "<link rel='icon' href='/CH/Icons/favicon-16x16.png' type='image/png' sizes='16x16'>")
    DOC.append("<meta name='robots' content='FOLLOW'>")
    DOC.append("<meta name='msapplication-TileColor' content='#2F2F2F'>")
    DOC.append(
        "<meta name='msapplication-TileImage' content='/CH/Icons/ms-icon-144x144.png'>")
    DOC.append("<meta name='theme-color' content='#2F2F2F'>")
    DOC.append("<meta property='og:title' content='View File " + Heading + "'/>")
    DOC.append("<meta property='og:type' content='website'/>")
    DOC.append("<meta property='og:url' content='" +
               ('https://' if os.environ['HTTPS'].lower() == 'on' else 'http://') + os.environ['HTTP_HOST'] + os.environ['REQUEST_URI'] + "'/>")
    DOC.append("")
    DOC.append("")
    DOC.append("")
    DOC.append("")
    DOC.append("")
    DOC.append("")
    DOC.append("")
    DOC.append('<link rel="stylesheet" href="/CH/CSS/' + stylesheet + '">')
    DOC.append("</head>")
    DOC.append("<body>")
    DOC.append("<div id='Wrapper'>")
    DOC.extend(InnerHTML)
    DOC.append("</div>")
    DOC.append("</body>")
    DOC.append("</html>")

    # <meta name='twitter:card' content='summary'/>
    # <meta name='twitter:site' content='@Darnel_Kumar'/>
    # <meta name='twitter:creator' content='@Darnel_Kumar'/>
    # <meta property='og:image' content='https://dev.darnel-k.uk/Images/OpenGraph.png'/>
    # <meta property='og:image:alt' content='Open Graph Site Home Page Preview Image'/>
    # <meta property='og:description' content='Development area of my site'/>
    # <meta property='og:locale' content='en_GB'/>

    DOC = '\n'.join(DOC)
    print("Content-type: text/html;charset=UTF-8\r\n\r\n")
    print(DOC)
