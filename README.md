git pull-request
================

Automatically check out github pull requests into their own branch.

Installation
------------

Copy the script to somewhere in your ``PATH`` and make it executable.
Set github.token to your github OAUTH token
    i.e. git config --global github.token OAUTH-TOKEN

If you need Python 3 support be sure to use the ``python3`` branch.

Usage
-----

    git pull-request <OPTIONS> [<pull request number>]

Options
-------

    -h, --help
        Display this message and exit

    -r <repo>, --repo <repo>
        Use this github repo instead of the 'remote origin' or 'github.repo'
        git config settings. Needs to be in "user/repository" form

License
=======

Copyright (C) 2011-2013 by Andreas Gohr <andi@splitbrain.org>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
