def _parse_args():
    parser = optparse.OptionParser()
    parser.add_option('--user', dest='user_install', action='store_true',
        default=False, help=
        'install in user site package (requires Python 2.6 or later)')
    parser.add_option('--download-base', dest='download_base', metavar=
        'URL', default=DEFAULT_URL, help=
        'alternative URL from where to download the setuptools package')
    parser.add_option('--insecure', dest='downloader_factory', action=
        'store_const', const=lambda : download_file_insecure, default=
        get_best_downloader, help='Use internal, non-validating downloader')
    options, args = parser.parse_args()
    return options