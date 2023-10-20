# SRM - Simple Regex Matcher

Purposefully simple CLI tool to match regex pattern against every line in a
given file or all files in a given directory recursively.

## Installation

```bash
git clone https://github.com/oliverwieges/srm.git
cd srm
pip install .
```

## Usage

```bash
# Search for regex in all files in current dir/subdirs ignoring .git/.venv.
srm ./ '(# TODO.*)' -I '^(.git).*' '.*(.venv).*'

# Search for regex in ./README.md only.
srm ./README.md '.*f[oif]o'
```
