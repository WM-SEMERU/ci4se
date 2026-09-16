def run():
    parser = OptionParser(version='%prog {0}'.format(__version__))
    parser.add_option('-a', '--addr', default='localhost', help=
        'The address or host to listen on. Specify -a 0.0.0.0 to listen on all addresses. Default: localhost'
        )
    parser.add_option('-p', '--port', type='int', default='10101', help=
        'The port to listen for requests on. Default: 10101')
    options, _ = parser.parse_args()
    try:
        server = ThreadingTCPServer((options.addr, options.port),
            RequestHandler)
    except (socket.error, socket.gaierror) as exc:
        print(exc)
        sys.exit(1)
    print('Listening on {0} port {1}'.format(options.addr, options.port))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        RequestHandler.http.close()
        print('Goodbye!')