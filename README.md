# File Handler

**Only For Apache 2.4+**

- [File Handler](#file-handler)
    - [URL Query Parameters:](#url-query-parameters)
        - [1. ### CH_FORMAT](#1--ch_format)
        - [2. ### CH_BRIGHTNESS](#2--ch_brightness)
    - [Requirements:](#requirements)
    - [Installation Instructions:](#installation-instructions)

## URL Query Parameters:

**Case Insensitive**

1.  ### CH_FORMAT

    > Purpose: Enables or disables function of this script
    >
    > **Some File Extensions are enabled by default making this parameter useless**
    >
    > Accepted Values
    >
    > -   On: 1, y, yes
    > -   Off: 0, n, no
    >
    > Example:
    >
    > > On:
    > >
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_FORMAT=1](https://hawk.kajida.uk/CH/README.md?CH_FORMAT=1)
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_FORMAT=y](https://hawk.kajida.uk/CH/README.md?CH_FORMAT=y)
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_FORMAT=yes](https://hawk.kajida.uk/CH/README.md?CH_FORMAT=yes)
    >
    > > Off:
    > >
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_FORMAT=0](https://hawk.kajida.uk/CH/README.md?CH_FORMAT=0)
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_FORMAT=n](https://hawk.kajida.uk/CH/README.md?CH_FORMAT=n)
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_FORMAT=no](https://hawk.kajida.uk/CH/README.md?CH_FORMAT=no)

2.  ### CH_BRIGHTNESS

    > Purpose: Controls whether light or dark theme is shown
    >
    > Accepted Values
    >
    > -   Dark Theme: 0, dark, d, night
    > -   Light Theme: 1, light, l, day
    >
    > Example:
    >
    > > Dark:
    > >
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=0](https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=0)
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=dark](https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=dark)
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=d](https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=d)
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=night](https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=night)
    >
    > > Light:
    > >
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=1](https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=1)
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=light](https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=light)
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=l](https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=l)
    > > -   [https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=day](https://hawk.kajida.uk/CH/README.md?CH_BRIGHTNESS=day)

## Requirements:

> -   Apache 2.4+
> -   Python 3.6+
> -   Python 3 Packages:
>     -   asciimatics
>     -   Markdown
>     -   markdown-checklist
>     -   MarkdownSubscript
>     -   MarkdownSuperscript
>     -   Pygments
>     -   python-magic

## Installation Instructions:

**You will require enough permissions on the host system to use git, make changes to the apache server configs and restart / reload the apache server**

**Python 3 MUST be installed on the server you wish to use this on!**

> 1.  Install all the python packages listed above.
>
> ```powershell
> pip install asciimatics Markdown markdown-checklist MarkdownSubscript MarkdownSuperscript Pygments python-magic
> ```
>
> 2.  Clone this repository to a directory inside the ServerRoot
> 3.  Create file "CH.conf" in Apache
