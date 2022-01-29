from xss import XssSanitizer

xss = """
<XSS STYLE="xss:expression(alert('XSS'))"> normal xss payload
"""

with XssSanitizer(xss) as sanitizer:
    print(sanitizer.sanitized)