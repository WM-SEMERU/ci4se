def is_equal(a, b, tol):
    if a == b or abs(a - b) <= tol * max(abs(a), abs(b)):
        return True
    else:
        return False