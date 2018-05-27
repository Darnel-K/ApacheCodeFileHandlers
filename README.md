# NSSTFAI

A Not So Simple Theme For Apache's Index

[View Changelog](CHANGELOG.md)

[Demo](http://rs01.kajida.uk/GitHub/Experimental-Code) showing a clone of one of my other repositories, setup globally.

This theme now has a name however if you have any other ideas please, leave your suggestions [here](https://github.com/Darnel-K/Apache-Index-Theme/issues/1).

- [NSSTFAI](#nsstfai)
    - [Installation Instructions:](#installation-instructions)
        - [Method 1 - Installing The Global Version (Requires Access To The Host System And Web Server)](#method-1---installing-the-global-version-requires-access-to-the-host-system-and-web-server)
        - [Method 2 - Installing The .htaccess version](#method-2---installing-the-htaccess-version)
    - [Variations:](#variations)
    - [Help:](#help)
    - [TO-DO:](#to-do)
    - [Resources Used:](#resources-used)

## Installation Instructions:

Both versions require "AllowOverride All" activated on the web server for the directories that use the ".htaccess" files.<br>

### Method 1 - Installing The Global Version (Requires Access To The Host System And Web Server)

**You will require enough permissions on the host system to use git, make changes to the apache server configs and restart / reload the apache server**

> This version will set this theme as the default for every directory in which indexing is active.
>
> 1.  Clone this repository to a directory inside the ServerRoot.
> 2.  Copy "IncludeTheme.conf.sample" to "IncludeTheme.conf"
> 3.  Edit lines 1 & 3 of "IncludeTheme.conf" changing "[ThemeFilesLocation]" to the location of the "NSSTFAI" folder.
> 4.  Edit line 9 of "IncludeTheme.conf" changing [ThemeConfLocation]" to the location of the "NSSTFAI.conf" file relative to the ServerRoot.
> 5.  Copy "IncludeTheme.conf" to the apache includes directory.
> 6.  Restart / Reload the apache server
> 7.  To activate the theme add "Options +Indexes" to the directory either in the server config file or inside a ".htaccess" file located in the directory to be indexed

### Method 2 - Installing The .htaccess version

> This version is only active on the directory that contains the required files and all sub-directories with indexing allowed.
>
> 1.  Download a copy of the folder "NSSTFAI" and the file ".htaccess".
> 2.  Copy, upload or move the folder "NSSTFAI" to your domain's root directory
> 3.  Copy, upload or move the file ".htaccess" to the folder you wish to enable indexing and directory listing on (This also applies to all nested directories). If copying, uploading or moving the ".htaccess" file to the root directory of the domain SKIP STEP 4.
> 4.  In the root directory create a ".htaccess" file and put "IndexIgnore .htaccess NSSTFAI" into it

## Variations:

*   [Dark (Default), Branch: MASTER](//github.com/Darnel-K/NSSTFAI/tree/master)

## Help:

*   Left Arrow / Backspace: Goes to the previous directory if available.
*   Right Arrow: Will enter / open the currently selected directory / file.
*   Up Arrow: Navigates the selector up one.
*   Down Arrow: Navigates the selector down one.
*   S Key: Toggles Settings Screen

## TO-DO:

*   [ ] Add Credits Screen
*   [ ] Video Player
*   [ ] Audio Player
*   [ ] Image Viewer
*   [x] Clean CSS
*   [x] Convert CSS To SASS
*   [ ] Create Unix .sh Installer
*   [ ] Create Windows .bat Installer
*   [ ] Add Help Screen
*   [ ] Acquire Logo For Theme
*   [ ] Logo Favicon
*   [x] Create Separate Layout For Desktop & Mobile
*   [x] Disable Some Features On Small Screens
*   [x] Make Responsive
*   [ ] Add Optional Table Header / Footer
*   [x] Redo The Update Check Code
*   [x] Rewrite Settings Screen HTML & JS
*   [x] Implement Console Logging Into The JS
*   [x] Pick A Name
*   [x] Rewrite The JS Settings
*   [x] Add Arrow Key Navigation
*   [x] Replace All Instances Of "ThemeName" With Chosen Name
*   [x] Upload Files To GitHub
*   [x] Create htaccess Directory Version
*   [x] Add Setup Instructions For Both Versions
*   [x] Cleanup Files & Remove Duplicates

## Resources Used:

*   [jscolor Color Picker](http://jscolor.com/)
*   [jQuery-rcrumbs Responsive Breadcrumb](https://github.com/cm0s/jquery-rcrumbs)
*   [jQuery.qrcode QR Code Generator](https://larsjung.de/jquery-qrcode/)
*   [jQuery](https://jquery.com/)
*   [Icons Used From Icons8](https://icons8.com/)

```
#!python
import markdown
import cgitb
import os
import re
from markdown.extensions.toc import TocExtension

cgitb.enable()

DIRNAME, FullFileName = os.path.split(os.environ['PATH_TRANSLATED'])
filename, file_extension = os.path.splitext(os.environ['PATH_TRANSLATED'])

InnerHTMLString = ""
DOC = []

with open(filename + file_extension, 'r') as f:
    InnerHTMLString = markdown.markdown(text=f.read(), output_format="html5", extensions=[
        'subscript', 'superscript', 'markdown_checklist.extension', 'markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.meta', 'markdown.extensions.nl2br', TocExtension(title="Contents:", anchorlink=True), 'markdown.extensions.codehilite'])

InnerHTML = InnerHTMLString.splitlines()
Heading = None
HeadSearch = re.search('<(h1)[\s>]', InnerHTML[0])
if (HeadSearch is not None):
    if (HeadSearch.group(1) == "h1"):
        Heading = re.search('<h1.*><a.*>(.*)<\/a><\/h1>',
                            InnerHTML[0]).group(1)

DOC.append("<!DOCTYPE html>")
DOC.append("<html>")
DOC.append("<head>")
DOC.append('<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">')
DOC.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
DOC.append('<link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i&amp;subset=latin-ext" rel="stylesheet">')
DOC.append('<link rel="stylesheet" href="/CodeHandler/CSS/MaterialDark.min.css">')
DOC.append("</head>")
DOC.append("<body>")

if (Heading is not None):
    InnerHTML.pop(0)
    DOC.append("<header>")
    DOC.append("<h1>" + Heading + "</h1>")
    DOC.append("</header>")
else:
    DOC.append("<header>")
    DOC.append("<h1>" + FullFileName + "</h1>")
    DOC.append("</header>")

DOC.append("<div id='Wrapper'>")
DOC.extend(InnerHTML)
DOC.append("</div>")
DOC.append("</body>")
DOC.append("</html>")

DOC = ''.join(DOC)
print("Content-type:text/html\r\n\r\n")
print(DOC)
```

-

```
import markdown
import cgitb
import os
import re
from markdown.extensions.toc import TocExtension

cgitb.enable()

DIRNAME, FullFileName = os.path.split(os.environ['PATH_TRANSLATED'])
filename, file_extension = os.path.splitext(os.environ['PATH_TRANSLATED'])

InnerHTMLString = ""
DOC = []

with open(filename + file_extension, 'r') as f:
InnerHTMLString = markdown.markdown(text=f.read(), output_format="html5", extensions=[
'subscript', 'superscript', 'markdown_checklist.extension', 'markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.meta', 'markdown.extensions.nl2br', TocExtension(title="Contents:", anchorlink=True), 'markdown.extensions.codehilite'])

InnerHTML = InnerHTMLString.splitlines()
Heading = None
HeadSearch = re.search('<(h1)[\s>]', InnerHTML[0])
if (HeadSearch is not None):
if (HeadSearch.group(1) == "h1"):
Heading = re.search('<h1._><a._>(.\*)<\/a><\/h1>',
InnerHTML[0]).group(1)

DOC.append("<!DOCTYPE html>")
DOC.append("<html>")
DOC.append("<head>")
DOC.append('<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">')
DOC.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
DOC.append('<link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i&amp;subset=latin-ext" rel="stylesheet">')
DOC.append('<link rel="stylesheet" href="/CodeHandler/CSS/MaterialDark.min.css">')
DOC.append("</head>")
DOC.append("<body>")

if (Heading is not None):
InnerHTML.pop(0)
DOC.append("<header>")
DOC.append("<h1>" + Heading + "</h1>")
DOC.append("</header>")
else:
DOC.append("<header>")
DOC.append("<h1>" + FullFileName + "</h1>")
DOC.append("</header>")

DOC.append("<div id='Wrapper'>")
DOC.extend(InnerHTML)
DOC.append("</div>")
DOC.append("</body>")
DOC.append("</html>")

DOC = ''.join(DOC)
print("Content-type:text/html\r\n\r\n")
print(DOC)
```
```
::-webkit-scrollbar{height:4px;width:4px}::-webkit-scrollbar-button{height:0px;width:0px}::-webkit-scrollbar-track{background:rgba(0,0,0,0.2);-webkit-border-radius:10px;border-radius:10px}::-webkit-scrollbar-thumb{background:#888;border:thin solid #808080;-webkit-border-radius:10px;border-radius:10px}::-webkit-scrollbar-thumb:hover{background:#666;border:thin solid #666}html,body{margin:0;padding:0}body{width:100vw;overflow-x:hidden;display:grid;font-family:Consolas,Monospace}body .checklist{list-style:none;padding:0 0 0 20px}body .checklist li input{vertical-align:middle}body img{max-height:250px;padding:10px}body a{text-decoration:none}body header{height:40px;padding:16px;width:-webkit-calc(100vw - (16px * 2));width:calc(100vw - (16px * 2));position:fixed;z-index:50;display:grid}body header h1{margin:0;line-height:40px;vertical-align:middle}body #Wrapper{padding:16px;width:-webkit-calc(100vw - (16px * 2));width:calc(100vw - (16px * 2));margin-top:-webkit-calc(40px + (16px * 2));margin-top:calc(40px + (16px * 2));display:grid;grid-template-columns:100%}body #Wrapper code{color:#FF931C;padding:3px 7px;-webkit-border-radius:3px;border-radius:3px}body #Wrapper .codehilite{overflow-x:auto;padding:10px;margin:10px}body #Wrapper .codehilite pre{margin:0}body #Wrapper hr{width:100%}body #Wrapper p{line-height:1.4}body #Wrapper blockquote{padding:0 10px;margin:10px;overflow:hidden}body #Wrapper blockquote,body #Wrapper .codehilite{width:-webkit-fill-available;width:-moz-available;width:fill-available;-webkit-border-radius:3px;border-radius:3px}body{color:#D4D4D4;background-color:#2F2F2F}body img{border-left:3px solid #FF3F3F}body a{color:#FF3F3F}body a:hover{color:#D4D4D4}body header{-webkit-box-shadow:0px -2px 20px 0px #3f3f3f;box-shadow:0px -2px 20px 0px #3f3f3f;background-color:#1F1F1F;color:#D4D4D4;border-bottom:3px solid #FF3F3F}body #Wrapper code{background-color:rgba(0,0,0,0.3)}body #Wrapper hr{border-color:#FF3F3F}body #Wrapper blockquote{background-color:rgba(70,70,70,0.4);border-left:3px solid #FF3F3F}body #Wrapper .codehilite{background:rgba(0,0,0,0.3);color:#d0d0d0}body #Wrapper .codehilite .hll{background-color:#404040}body #Wrapper .codehilite .c{color:#999999;font-style:italic}body #Wrapper .codehilite .err{color:#a61717;background-color:#e3d2d2}body #Wrapper .codehilite .esc{color:#d0d0d0}body #Wrapper .codehilite .g{color:#d0d0d0}body #Wrapper .codehilite .k{color:#6ab825;font-weight:bold}body #Wrapper .codehilite .l{color:#d0d0d0}body #Wrapper .codehilite .n{color:#d0d0d0}body #Wrapper .codehilite .o{color:#d0d0d0}body #Wrapper .codehilite .x{color:#d0d0d0}body #Wrapper .codehilite .p{color:#d0d0d0}body #Wrapper .codehilite .ch{color:#999999;font-style:italic}body #Wrapper .codehilite .cm{color:#999999;font-style:italic}body #Wrapper .codehilite .cp{color:#cd2828;font-weight:bold}body #Wrapper .codehilite .cpf{color:#999999;font-style:italic}body #Wrapper .codehilite .c1{color:#999999;font-style:italic}body #Wrapper .codehilite .cs{color:#e50808;font-weight:bold;background-color:#520000}body #Wrapper .codehilite .gd{color:#d22323}body #Wrapper .codehilite .ge{color:#d0d0d0;font-style:italic}body #Wrapper .codehilite .gr{color:#d22323}body #Wrapper .codehilite .gh{color:#ffffff;font-weight:bold}body #Wrapper .codehilite .gi{color:#589819}body #Wrapper .codehilite .go{color:#cccccc}body #Wrapper .codehilite .gp{color:#aaaaaa}body #Wrapper .codehilite .gs{color:#d0d0d0;font-weight:bold}body #Wrapper .codehilite .gu{color:#ffffff;text-decoration:underline}body #Wrapper .codehilite .gt{color:#d22323}body #Wrapper .codehilite .kc{color:#6ab825;font-weight:bold}body #Wrapper .codehilite .kd{color:#6ab825;font-weight:bold}body #Wrapper .codehilite .kn{color:#6ab825;font-weight:bold}body #Wrapper .codehilite .kp{color:#6ab825}body #Wrapper .codehilite .kr{color:#6ab825;font-weight:bold}body #Wrapper .codehilite .kt{color:#6ab825;font-weight:bold}body #Wrapper .codehilite .ld{color:#d0d0d0}body #Wrapper .codehilite .m{color:#3677a9}body #Wrapper .codehilite .s{color:#ed9d13}body #Wrapper .codehilite .na{color:#bbbbbb}body #Wrapper .codehilite .nb{color:#24909d}body #Wrapper .codehilite .nc{color:#447fcf;text-decoration:underline}body #Wrapper .codehilite .no{color:#40ffff}body #Wrapper .codehilite .nd{color:#ffa500}body #Wrapper .codehilite .ni{color:#d0d0d0}body #Wrapper .codehilite .ne{color:#bbbbbb}body #Wrapper .codehilite .nf{color:#447fcf}body #Wrapper .codehilite .nl{color:#d0d0d0}body #Wrapper .codehilite .nn{color:#447fcf;text-decoration:underline}body #Wrapper .codehilite .nx{color:#d0d0d0}body #Wrapper .codehilite .py{color:#d0d0d0}body #Wrapper .codehilite .nt{color:#6ab825;font-weight:bold}body #Wrapper .codehilite .nv{color:#40ffff}body #Wrapper .codehilite .ow{color:#6ab825;font-weight:bold}body #Wrapper .codehilite .w{color:#666666}body #Wrapper .codehilite .mb{color:#3677a9}body #Wrapper .codehilite .mf{color:#3677a9}body #Wrapper .codehilite .mh{color:#3677a9}body #Wrapper .codehilite .mi{color:#3677a9}body #Wrapper .codehilite .mo{color:#3677a9}body #Wrapper .codehilite .sa{color:#ed9d13}body #Wrapper .codehilite .sb{color:#ed9d13}body #Wrapper .codehilite .sc{color:#ed9d13}body #Wrapper .codehilite .dl{color:#ed9d13}body #Wrapper .codehilite .sd{color:#ed9d13}body #Wrapper .codehilite .s2{color:#ed9d13}body #Wrapper .codehilite .se{color:#ed9d13}body #Wrapper .codehilite .sh{color:#ed9d13}body #Wrapper .codehilite .si{color:#ed9d13}body #Wrapper .codehilite .sx{color:#ffa500}body #Wrapper .codehilite .sr{color:#ed9d13}body #Wrapper .codehilite .s1{color:#ed9d13}body #Wrapper .codehilite .ss{color:#ed9d13}body #Wrapper .codehilite .bp{color:#24909d}body #Wrapper .codehilite .fm{color:#447fcf}body #Wrapper .codehilite .vc{color:#40ffff}body #Wrapper .codehilite .vg{color:#40ffff}body #Wrapper .codehilite .vi{color:#40ffff}body #Wrapper .codehilite .vm{color:#40ffff}body #Wrapper .codehilite .il{color:#3677a9}
/*# sourceMappingURL=Dark.min.css.map */
```
