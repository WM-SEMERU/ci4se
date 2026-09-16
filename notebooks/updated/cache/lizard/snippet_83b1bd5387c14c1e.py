def start_recv(sockfile=None):
    if sockfile is not None:
        SOCKFILE = sockfile
    else:
        SOCKFILE = '/tmp/snort_alert'
    if os.path.exists(SOCKFILE):
        os.unlink(SOCKFILE)
    unsock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    unsock.bind(SOCKFILE)
    logging.warning('Unix socket start listening...')
    while True:
        data = unsock.recv(BUFSIZE)
        parsed_msg = alert.AlertPkt.parser(data)
        if parsed_msg:
            yield parsed_msg