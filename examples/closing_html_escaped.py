from xss import XssSanitizer

xss = """
&#00;</form><input type&#61;"date" onfocus="alert(1)">
"""

with XssSanitizer(xss) as sanitizer:
    print(sanitizer.sanitized)