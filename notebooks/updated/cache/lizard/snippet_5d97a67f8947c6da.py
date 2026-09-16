def main():
    parser = OptionParser()
    parser.add_option('-c', '--config', help='configuration file', dest=
        'filename', type='str', default=
        '/etc/sachannelupdate/sachannelupdate.ini')
    parser.add_option('-d', '--delete', help='Deletes existing rules', dest
        ='cleanup', action='store_true', default=False)
    options, _ = parser.parse_args()
    if not os.path.isfile(options.filename):
        raise SaChannelUpdateConfigError(
            'The configuration file: %s does not exist' % options.filename)
    config = ConfigParser()
    config.read(options.filename)
    try:
        entry(config._sections['settings'], options.cleanup)
    except BaseException as msg:
        error(msg)