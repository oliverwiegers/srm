#!/usr/bin/env python3
"""SRM - Simple Regex Matcher

Purposefully simple CLI tool to match regex pattern against every line in a
given file or all files in a given directory recursively.

Typical usage:
    $ srm ./ '(# TODO.*)' -I '^(.git).*' '.*(.venv).*' 
    $ srm ./README.md '.*f[oif]o'
"""

import re
import sys
import argparse
import pathlib


def match_pattern(filepath: str, regex: str):
    """Search for regex in file.

    Match regex pattern agains every line in given file.

    Args:
        filepath:   Path of file to search for regex in.
        regex:      Regex pattern to search for in file.
    """
    regex_obj = re.compile(regex)
    try:
        with open(filepath, encoding="utf-8") as handle:
            # Find all matches for given regex in every line of a file.
            # Than print the filepath, linenumber and regex match to stdout.
            list(
                map(
                    lambda x_y: list(
                        map(
                            lambda match: print(
                                f"{filepath}:{x_y[0]}: \033[92m{match}\033[0m"
                            ),
                            regex_obj.findall(x_y[1]),
                        )
                    ),
                    enumerate(handle, 1),
                )
            )
    # Ignore errors from trying to read binary files.
    except UnicodeDecodeError:
        pass


def find_files(path: str, exclude: list) -> list[str]:
    """Find all files to search in.

    Finds all files in a given path. And filters out all files contained in the
    exclude list.

    Args:
        path:       Path to search for files in.
        exclude:    List of regexes for paths to exclude from search.

    Returns:
        A list of strings containing all files in given path. Filtered out the
        excludes.
    """
    path_obj = pathlib.Path(path)
    files = list(filter(lambda path: path.is_file(), path_obj.rglob("*")))

    if exclude:
        combined_regex = re.compile("(" + ")|(".join(exclude) + ")")
        return list(filter(lambda file: not re.match(combined_regex, str(file)), files))

    return files


def main():
    """Console entry point.

    Parse cli arguments and start pattern matching accordingly.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Path of file or directory to search in.")
    parser.add_argument("regex", help="Regex to search for in file[s].")
    parser.add_argument(
        "-e",
        "--exclude",
        type=str,
        nargs="*",
        help="Space separated list of regexes for files to exclude.",
    )
    args = parser.parse_args()

    if pathlib.Path(args.path).is_file():
        match_pattern(args.path, args.regex)
    elif pathlib.Path(args.path).is_dir():
        list(
            map(
                lambda x: match_pattern(x, args.regex),
                find_files(args.path, args.exclude),
            )
        )
    else:
        print(
            f"File: {args.path} is a neither a file nor a directory. Skipping...",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
