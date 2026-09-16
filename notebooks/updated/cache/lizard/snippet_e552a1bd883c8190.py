def print_exception(etype, value, tb, limit=None, file=None, chain=True):
    import traceback
    if file is None:
        file = sys.stderr
    if tb:
        file.write('Traceback (most recent call last):\n')
        print_tb(tb, limit, file)
    lines = traceback.format_exception_only(etype, value)
    for line in lines:
        file.write(line)