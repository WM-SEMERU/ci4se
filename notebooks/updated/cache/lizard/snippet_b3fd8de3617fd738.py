def list_and_add(a, b):
    if not isinstance(b, list):
        b = [b]
    if not isinstance(a, list):
        a = [a]
    return a + b