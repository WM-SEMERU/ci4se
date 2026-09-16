def chkpath(path):
    if os.path.exists(path):
        return path
    else:
        msg = '{0} does not exist.'.format(path)
        raise argparse.ArgumentTypeError(msg)