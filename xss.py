import re
import html
from urllib.parse import unquote_plus

class XssSanitizer:
    def __init__(self, string: str) -> None:
        self.string = string.strip().strip('\n\r')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def __url_encode_break__(self) -> None:
        while True:
            self.string = html.unescape(unquote_plus(self.string))
            if '%' not in self.string:
                break
        return

    def __html_escape_break__(self) -> None:
        while True:
            self.string = html.unescape(self.string)
            if "&" not in self.string:
                break
        return

    @property
    def sanitized(self) -> str:
        tags = re.compile(r"(?:(?:\"|\')\>)*?(?:\<(?:.*)\>)*?(?:\<\/(?:.*)\>)*?", re.MULTILINE | re.IGNORECASE)
        if '%' in self.string:
            self.__url_encode_break__()
        if "&" in self.string:
            self.__html_escape_break__()
        cleansed = html.unescape(self.string)
        repl = tags.sub('', cleansed)
        return repl