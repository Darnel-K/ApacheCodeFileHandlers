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

    This version is only active on the directory that contains the required files and all sub-directories with indexing allowed.

    1.  Download a copy of the folder "NSSTFAI" and the file ".htaccess".
    2.  Copy, upload or move the folder "NSSTFAI" to your domain's root directory
    3.  Copy, upload or move the file ".htaccess" to the folder you wish to enable indexing and directory listing on (This also applies to all nested directories). If copying, uploading or moving the ".htaccess" file to the root directory of the domain SKIP STEP 4.
    4.  In the root directory create a ".htaccess" file and put "IndexIgnore .htaccess NSSTFAI" into it

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
                'markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.meta', 'markdown.extensions.nl2br', TocExtension(title="Contents:", anchorlink=True), 'markdown.extensions.codehilite'])

        DOC = """<!DOCTYPE html>
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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

```
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
        'markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.meta', 'markdown.extensions.nl2br', TocExtension(title="Contents:", anchorlink=True), 'markdown.extensions.codehilite'])

DOC = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
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
```
