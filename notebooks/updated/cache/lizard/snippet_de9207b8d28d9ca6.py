def file_arg(arg):
    prefix = 'file://'
    if arg.startswith(prefix):
        return os.path.abspath(arg[len(prefix):])
    else:
        msg = 'Invalid file argument "{}", does not begin with "file://"'
        raise argparse.ArgumentTypeError(msg.format(arg))