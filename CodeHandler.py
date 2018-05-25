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
        'superscript', 'markdown_checklist.extension', 'markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.meta', 'markdown.extensions.nl2br', TocExtension(title="Contents:", anchorlink=True), 'markdown.extensions.codehilite'])

DOC = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<link rel="stylesheet" href="/CodeHandler/CSS/Native.css">
<link rel="stylesheet" href="/CodeHandler/CSS/Main.min.css">
</head>
<body>
""" + InnerHTML + """
</body>
</html>"""

# # file = open(file="output.html", mode="w", encoding="utf-8")
# # file.write(DOC)
# # file.close()

print("Content-type:text/html\r\n\r\n")
print(DOC)
