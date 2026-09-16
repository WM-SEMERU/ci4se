def parse_options():
    parser = argparse.ArgumentParser(description=
        'Video downloader by radzak.', prog='RTVdownloader')
    urls_group = parser.add_mutually_exclusive_group(required=True)
    urls_group.add_argument('urls', type=str, metavar='URL', default=[],
        nargs='*', help='urls of sites containing videos you wish to download')
    urls_group.add_argument('-f', type=argparse.FileType('r'), dest='files',
        metavar='FILE', default=[], nargs='*', help=
        'text file with urls of sites containing videos you wish to download ')
    urls_group.add_argument('-o', type=str, dest='onetabs', metavar=
        'ONETAB', default=[], nargs='*', help=
        'onetab links containing urls of the videos you wish to download')
    options = DEFAULT_OPTIONS
    args = parser.parse_args()
    return options, args