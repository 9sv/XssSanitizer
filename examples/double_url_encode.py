from xss import XssSanitizer

xss = """
%253cscript%253ealert(1)%253c/script%253e double url encode
"""

with XssSanitizer(xss) as sanitizer:
    print(sanitizer.sanitized)