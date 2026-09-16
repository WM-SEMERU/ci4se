def main():
    from optparse import OptionParser
    parser = OptionParser('Start mock MongoDB server')
    parser.add_option('-p', '--port', dest='port', default=27017, help=
        'port on which mock mongod listens')
    parser.add_option('-q', '--quiet', action='store_false', dest='verbose',
        default=True, help="don't print messages to stdout")
    options, cmdline_args = parser.parse_args()
    if cmdline_args:
        parser.error('Unrecognized argument(s): %s' % ' '.join(cmdline_args))
    server = interactive_server(port=options.port, verbose=options.verbose)
    try:
        server.run()
        print('Listening on port %d' % server.port)
        time.sleep(1000000.0)
    except KeyboardInterrupt:
        server.stop()