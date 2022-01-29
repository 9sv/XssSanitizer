from xss import XssSanitizer

xss = """
"`'><script>\xE2\x80\x88javascript:alert(1)</script> closing tag hex coded
"""

with XssSanitizer(xss) as sanitizer:
    print(sanitizer.sanitized)