def invalid_marker(text):
    try:
        evaluate_marker(text)
    except SyntaxError as e:
        e.filename = None
        e.lineno = None
        return e
    return False