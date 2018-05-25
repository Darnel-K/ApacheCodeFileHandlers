#!/usr/local/bin/python3.6

import markdown
import cgitb
import os
from markdown.extensions.toc import TocExtension

cgitb.enable()

filename, file_extension = os.path.splitext(os.environ['PATH_TRANSLATED'])

InnerHTML = ""

with open(filename + file_extension, 'r') as f:
    InnerHTML = markdown.markdown(text=f.read(), output_format="html5", extensions=[
        'subscript', 'superscript', 'markdown_checklist.extension', 'markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.meta', 'markdown.extensions.nl2br', TocExtension(title="Contents:", anchorlink=True), 'markdown.extensions.codehilite'])

DOC = """<!DOCTYPE html>
<html>
<head>
<link href="//fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link type="text/css" rel="stylesheet" href="/CodeHandler/CSS/materialize.min.css"  media="screen,projection"/>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="stylesheet" href="/CodeHandler/CSS/MaterialLight.min.css">
</head>
<body>""" + InnerHTML + """<script type="text/javascript" src="/CodeHandler/JS/materialize.min.js"></script>
</body>
</html>"""

# # file = open(file="output.html", mode="w", encoding="utf-8")
# # file.write(DOC)
# # file.close()

print("Content-type:text/html\r\n\r\n")
print(DOC)
