#!/usr/local/bin/python3.6

import markdown
import os
from markdown.extensions.toc import TocExtension

InnerHTML = ""

with open(os.environ['PATH_TRANSLATED'], 'r') as f:
    InnerHTML = markdown.markdown(text=f.read(), output_format="html5", extensions=[
        'markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.meta', 'markdown.extensions.nl2br', TocExtension(title="Contents:", anchorlink=True)])

DOC = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="CSS/Markdown.min.css">
<!-- <link rel="stylesheet" href="//raw.githubusercontent.com/Darnel-K/Experimental-Code/master/Python%203/Markdown-Processor/CSS/Markdown.min.css"> -->
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
