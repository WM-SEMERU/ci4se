def existing_path(value):
    if os.path.exists(value):
        return value
    else:
        raise argparse.ArgumentTypeError('Path {0} not found'.format(value))