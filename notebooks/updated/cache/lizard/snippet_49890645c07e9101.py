def diff(a, b):
    return ''.join(Differ().compare(a.splitlines(keepends=True), b.
        splitlines(keepends=True)))