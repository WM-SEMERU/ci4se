def ip_to_url(ip_addr):
    try:
        return socket.gethostbyaddr(ip_addr)[0]
    except (socket.gaierror, socket.herror):
        logger.exception('Could not resolve hostname')