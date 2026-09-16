def build_parser():
    parser = argparse.ArgumentParser(description='The IOTile task supervisor')
    parser.add_argument('-c', '--config', help='config json with options')
    parser.add_argument('-v', '--verbose', action='count', default=0, help=
        'Increase logging verbosity')
    return parser