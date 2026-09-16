def swallow_stdout(stream=None):
    saved = sys.stdout
    if stream is None:
        stream = StringIO()
    sys.stdout = stream
    try:
        yield
    finally:
        sys.stdout = saved