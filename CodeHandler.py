#!/usr/local/bin/python3.6

import markdown
import cgitb
import os
import re
from markdown.extensions.toc import TocExtension
from markdown.extensions.codehilite import CodeHiliteExtension

cgitb.enable()

ALLOWED_EXTENSIONS = []
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
Heading = None
DOC = []
f = open(FILENAME + FILE_EXTENSION, 'r')


def FormatFile(text, extension):
    global Heading
    if (extension == ".md"):
        InnerHTML = markdown.markdown(
            text=text, output_format="html5", extensions=EXTENSIONS).splitlines()
        if (Heading is None):
            search = re.search('<(h1)[\s>]', InnerHTML[0])
            if (search is not None & search.group(1) == "h1"):
                Heading = re.search(
                    '<h1.*><a.*>(.*)<\/a><\/h1>', InnerHTML[0]).group(1)
                InnerHTML.pop(0)
        return InnerHTML
    elif (extension in ALLOWED_EXTENSIONS):
        pass
    else:
        raise NotImplementedError("File Type Not Supported Yet!")
    if (Heading is None):
        Heading = FULL_FILE_NAME


InnerHTML = FormatFile(f.read(), FILE_EXTENSION)

DOC.append("<!DOCTYPE html>")
DOC.append("<html>")
DOC.append("<head>")
DOC.append("<title>" + Heading + "</title>")
DOC.append('<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">')
# DOC.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
# DOC.append('<link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i&amp;subset=latin-ext" rel="stylesheet">')
DOC.append('<link rel="stylesheet" href="/CodeHandler/CSS/Dark.min.css">')
# DOC.append('<link rel="stylesheet" href="/CodeHandler/CSS/Light.min.css">')
DOC.append("</head>")
DOC.append("<body>")
DOC.append("<header>")
DOC.append("<h1>" + Heading + "</h1>")
DOC.append("</header>")
DOC.append("<div id='Wrapper'>")
DOC.extend(InnerHTML)
# DOC.append(InnerHTMLString)
DOC.append("</div>")
DOC.append("</body>")
DOC.append("</html>")

DOC = '\n'.join(DOC)
print("Content-type:text/html\r\n\r\n")
print(DOC)
