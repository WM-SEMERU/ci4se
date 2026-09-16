def print_exception(*args, file=None, **kwargs):
    for line in format_exception(*args, **kwargs):
        vtml.vtmlprint(line, file=file)