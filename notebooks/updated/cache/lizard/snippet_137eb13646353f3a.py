def port(port):
    value = int(port)
    if value <= 0 or value > 65535:
        raise argparse.ArgumentTypeError('%s must be between [1 - 65535]' %
            port)
    return value