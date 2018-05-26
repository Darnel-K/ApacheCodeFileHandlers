#!/usr/local/bin/python3.6

# import markdown
# import cgitb
# import os
# import re
# from markdown.extensions.toc import TocExtension

# cgitb.enable()

# DIRNAME, FullFileName = os.path.split(os.environ['PATH_TRANSLATED'])
# filename, file_extension = os.path.splitext(os.environ['PATH_TRANSLATED'])

# InnerHTMLString = ""
# DOC = []

# with open(filename + file_extension, 'r') as f:
#     InnerHTMLString = markdown.markdown(text=f.read(), output_format="html5", extensions=[
#         'subscript', 'superscript', 'markdown_checklist.extension', 'markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.meta', 'markdown.extensions.nl2br', TocExtension(title="Contents:", anchorlink=True), 'markdown.extensions.codehilite'])

# InnerHTML = InnerHTMLString.splitlines()
# Heading = None
# HeadSearch = re.search('<(h1)[\s>]', InnerHTML[0])
# if (HeadSearch is not None):
#     if (HeadSearch.group(1) == "h1"):
#         Heading = re.search('<h1.*><a.*>(.*)<\/a><\/h1>',
#                             InnerHTML[0]).group(1)

# DOC.append("<!DOCTYPE html>")
# DOC.append("<html>")
# DOC.append("<head>")
# DOC.append('<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">')
# DOC.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
# DOC.append('<link rel="stylesheet" href="/CodeHandler/CSS/MaterialDark.min.css">')
# DOC.append("</head>")
# DOC.append("<body>")

# if (Heading is not None):
#     InnerHTML.pop(0)
#     DOC.append("<header>")
#     DOC.append("<h1>" + Heading + "</h1>")
#     DOC.append("</header>")
# else:
#     DOC.append("<header>")
#     DOC.append("<h1>" + FullFileName + "</h1>")
#     DOC.append("</header>")

# DOC.append("<div id='Wrapper'>")
# DOC.extend(InnerHTML)
# # DOC.append(InnerHTMLString)
# DOC.append("</div>")
# DOC.append("</body>")
# DOC.append("</html>")

# DOC = '\n'.join(DOC)
# print("Content-type:text/html\r\n\r\n")
# print(DOC)


import markdown
import os
from markdown.extensions.toc import TocExtension

InnerHTML = ""

with open(os.environ['PATH_TRANSLATED'], 'r') as f:
    InnerHTML = markdown.markdown(text=f.read(), output_format="html5", extensions=[
                                  'markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.meta', 'markdown.extensions.nl2br', TocExtension(title="Contents:", anchorlink=True), 'markdown.extensions.codehilite'])

DOC = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="/CodeHandler/CSS/MaterialDark.min.css">
<!-- <link rel="stylesheet" href="//raw.githubusercontent.com/Darnel-K/Experimental-Code/master/Python%203/Markdown-Processor/CSS/Markdown.min.css"> -->
</head>
<body>
""" + InnerHTML + """
</body>
</html>"""

# file = open(file="output.html", mode="w", encoding="utf-8")
# file.write(DOC)
# file.close()

print("Content-type:text/html\r\n\r\n")
print(DOC)
