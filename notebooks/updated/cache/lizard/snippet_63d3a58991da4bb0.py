def diff_texts(a, b, filename):
    a = a.splitlines()
    b = b.splitlines()
    return difflib.unified_diff(a, b, filename, filename, '(original)',
        '(refactored)', lineterm='')