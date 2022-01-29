from xss import XssSanitizer

xss = """
&lt;META HTTP-EQUIV=\"refresh\" CONTENT=\"0;url=javascript&#058;alert('XSS');\"&gt; html escaped
"""

with XssSanitizer(xss) as sanitizer:
    print(sanitizer.sanitized)