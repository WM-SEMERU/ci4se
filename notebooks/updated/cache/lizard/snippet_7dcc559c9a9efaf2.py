def get_argparser(parser=None):
    parser = parser or argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0', help='Host listen address'
        )
    parser.add_argument('--port', '-p', default=9050, help='Listen port',
        type=int)
    parser.add_argument('--debug', '-d', default=False, action='store_true',
        help='Enable debug mode')
    parser.add_argument('--log-level', '-l', default='INFO', help=
        'Log Level, empty string to disable.')
    parser.add_argument('--twisted', default=False, action='store_true',
        help='Use twisted to server requests.')
    parser.add_argument('--gunicorn', default=False, action='store_true',
        help='Use gunicorn to server requests.')
    parser.add_argument('--threads', default=None, help=
        'Number of threads to use.', type=int)
    parser.add_argument('--disable-embedded-logging', default=False, action
        ='store_true', help='Disable embedded logging configuration')
    return parser