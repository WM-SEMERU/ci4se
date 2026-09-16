def tcp_client(tcp_addr):
    family = socket.AF_INET6 if ':' in tcp_addr.ip else socket.AF_INET
    sock = socket.socket(family, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    for i in range(300):
        logging.info('Connecting to: %s, attempt %d', tcp_addr, i)
        try:
            sock.connect(tcp_addr)
            break
        except socket.error:
            time.sleep(1)
    else:
        sock.connect(tcp_addr)
    logging.info('Connected.')
    map_data = read_tcp(sock)
    settings_str = read_tcp(sock)
    if not settings_str:
        raise socket.error('Failed to read')
    settings = json.loads(settings_str.decode())
    logging.info('Got settings. map_name: %s.', settings['map_name'])
    logging.debug('settings: %s', settings)
    settings['map_data'] = map_data
    return sock, settings