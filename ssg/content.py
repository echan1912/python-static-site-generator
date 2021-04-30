from yaml import re, load, FullLoader
from collections.abc import Mapping

class content.Mapping:
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(
        __delimiter, re.MULTILINE
    )
    def load(cls, string):
        pass 