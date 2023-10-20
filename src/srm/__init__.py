"""SRM - Simple Regex Matcher.

Purposefully simple CLI tool to match regex pattern against every line in a
given file or all files in a given directory recursively.

Typical usage:
    $ srm ./ '(# TODO.*)' -I '^(.git).*' '.*(.venv).*'
    $ srm ./README.md '.*f[oif]o'
"""
