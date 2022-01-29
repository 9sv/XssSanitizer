from xss import XssSanitizer

xss = """
"><s"%2b"cript>alert(document.cookie)</script> closing tag and try to bypass anti-script tag
"""

with XssSanitizer(xss) as sanitizer:
    print(sanitizer.sanitized)