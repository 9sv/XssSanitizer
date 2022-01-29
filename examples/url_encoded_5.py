from xss import XssSanitizer

xss = """
%252525253cscript%252525253ealert%2525281%252529%252525253c%25252Fscript%252525253e url encoded 5 times
"""

with XssSanitizer(xss) as sanitizer:
    print(sanitizer.sanitized)