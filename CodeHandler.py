#!/usr/local/bin/python3.6

import cgitb
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

ALWAYS_ACTIVE = [".md", ".txt", ".sql", ".java", ".cs", ".py"]
FORMAT_QUERY = "CH_FORMAT"
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
Heading = None
DOC = []
STYLED_EXTENSIONS = [".txt"]
f = open(FILENAME + FILE_EXTENSION, 'r')


def FormatFile(text, extension):
    global Heading
    InnerHTML = None
    if (extension == ".md"):
        InnerHTML = markdown.markdown(
            text=text, output_format="html5", extensions=EXTENSIONS).splitlines()
        if (Heading is None):
            search = re.search('<(h1)[\s>]', InnerHTML[0])
            if (search is not None):
                if (search.group(1) == "h1"):
                    Heading = re.search(
                        '<h1.*><a.*>(.*)<\/a><\/h1>', InnerHTML[0]).group(1)
                    InnerHTML.pop(0)
    else:
        code = text
        lexer = guess_lexer_for_filename(FULL_FILE_NAME, code)
        formatter = HtmlFormatter(linenos=False, cssclass="codehilite")
        result = highlight(code, lexer, formatter)
        InnerHTML = [result]
    if (Heading is None):
        Heading = FULL_FILE_NAME
    return InnerHTML


FileOutput = f.read()
if ((FORMAT_QUERY not in URL_QUERY or (FORMAT_QUERY in URL_QUERY and (URL_QUERY[FORMAT_QUERY][0].lower() not in [1, "1", "yes", "y"]))) and FILE_EXTENSION not in ALWAYS_ACTIVE):
    m = magic.Magic(mime=True)
    # mime = (m.from_file(FILENAME + FILE_EXTENSION), None)
    # mime = mimetypes.guess_type(FULL_FILE_NAME, strict=False)
    mime = (None,)
    if (mime[0] == None):
        mime = ("application/octet-stream", None)
    print("Content-type: " + mime[0] + ";charset=UTF-8\r\n\r\n")
    # print(m.from_file(FILENAME + FILE_EXTENSION))
    print(FileOutput)
else:
    InnerHTML = FormatFile(FileOutput, FILE_EXTENSION)
    if ("CH_BRIGHTNESS" in URL_QUERY):
        if (URL_QUERY["CH_BRIGHTNESS"][0].lower() in [1, "1", "light", "l"]):
            stylesheet = "LIGHT"
        else:
            stylesheet = "DARK"
    else:
        stylesheet = "DARK"

    DOC.append("<!DOCTYPE html>")
    DOC.append("<html>")
    DOC.append("<head>")
    DOC.append("<title>" + Heading + "</title>")
    DOC.append(
        '<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">')
    # DOC.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    # DOC.append('<link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i&amp;subset=latin-ext" rel="stylesheet">')
    DOC.append('<link rel="stylesheet" href="/CH/CSS/' +
               stylesheet + '.min.css">')
    DOC.append("</head>")
    DOC.append("<body>")
    DOC.append("<header>")
    DOC.append("<h1>" + Heading + "</h1>")
    DOC.append("</header>")
    DOC.append("<div id='Wrapper'>")
    DOC.extend(InnerHTML)
    DOC.append("</div>")
    DOC.append("</body>")
    DOC.append("</html>")

    DOC = '\n'.join(DOC)
    print("Content-type:text/html\r\n\r\n")
    print(DOC)
