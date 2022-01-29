from xss import XssSanitizer

xss = """
%22%3E%3Cimg%20src%3Dx%20onerror%3Dwindow.open%28%27https%3A%2F%2Fwww.google.com%2F%27%29%3B%3E closing tag url encoded
"""

with XssSanitizer(xss) as sanitizer:
    print(sanitizer.sanitized)