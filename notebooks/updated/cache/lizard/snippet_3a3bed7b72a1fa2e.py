def to_existing_absolute_path(string):
    value = os.path.abspath(string)
    if not os.path.exists(value) or not os.path.isdir(value):
        msg = '"%r" is not a valid path to a directory.' % string
        raise argparse.ArgumentTypeError(msg)
    return value