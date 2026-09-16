def info(text, *args, **kwargs):
    text = text.format(*args, **kwargs)
    print(' '.join((purple('>>>'), text)))
    sys.stdout.flush()