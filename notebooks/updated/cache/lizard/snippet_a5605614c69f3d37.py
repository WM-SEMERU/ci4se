def _fetch_socket_data(self, parsed_url):
    self.log.debug('Fetching haproxy stats from socket: %s' % parsed_url.
        geturl())
    if parsed_url.scheme == 'tcp':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        splitted_loc = parsed_url.netloc.split(':')
        host = splitted_loc[0]
        port = int(splitted_loc[1])
        sock.connect((host, port))
    else:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(parsed_url.path)
    sock.send(b'show stat\r\n')
    response = ''
    output = sock.recv(BUFSIZE)
    while output:
        response += output.decode('ASCII')
        output = sock.recv(BUFSIZE)
    sock.close()
    return response.splitlines()