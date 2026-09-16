def run(argv=None):
    import sys
    import os
    import docopt
    import textwrap
    if not sys.version_info >= (3, 4):
        print('This python version is not supported. Please use python 3.4')
        exit(1)
    argv = argv or sys.argv[1:]
    docblock = run.__doc__.replace('::', ':')
    args = docopt.docopt(textwrap.dedent(docblock), argv)
    if args['--version']:
        print('httpserver version {} by {}'.format(__version__, __author__))
        exit(0)
    level = logging.WARNING
    if args['--verbose']:
        level = logging.INFO
    if args['--debug']:
        level = logging.DEBUG
    logging.basicConfig(level=level)
    logger = logging.getLogger('run method')
    logger.debug('CLI args: %s' % args)
    bindaddr = args['--bindaddress'] or '127.0.0.1'
    port = args['--port'] or '8080'
    folder = args['<folder>'] or os.getcwd()
    hostname = args['--host'] or 'localhost'
    _start_server(bindaddr, port, hostname, folder)