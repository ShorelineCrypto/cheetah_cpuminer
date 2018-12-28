import sys

# Safety for cases when shebang is bypassed.
assert sys.version_info[0] == 2 and sys.version_info[1] >= 7, 'Python version 2.7 (or a later 2.x version) required; you have version: {}.{}.{}'.format (*sys.version_info[0:3])
