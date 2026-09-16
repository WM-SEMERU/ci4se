def buildParser():
    parser = argparse.ArgumentParser(description=
        'Script to parse bagfile to csv file')
    parser.add_argument('bag', help='Bag file to read', type=str)
    parser.add_argument('-i', '--include', help=
        'list or regex for topics to include', nargs='*')
    parser.add_argument('-e', '--exclude', help=
        'list or regex for topics to exclude', nargs='*')
    parser.add_argument('-o', '--output', help='name of the output file',
        nargs='*')
    parser.add_argument('-f', '--fill', help=
        'Fill the bag forward and backwards so no missing values when present',
        action='store_true')
    parser.add_argument('--include-header', help=
        'Include the header fields.  By default they are excluded', action=
        'store_true')
    return parser