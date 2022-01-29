from xss import XssSanitizer

xss = """
"><img src=x onerror=window.open('https://www.google.com/');> closing tag
"""

with XssSanitizer(xss) as sanitizer:
    print(sanitizer.sanitized)