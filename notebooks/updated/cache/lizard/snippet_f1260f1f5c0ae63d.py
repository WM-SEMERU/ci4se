def _get_local_ip():
    return set([x[4][0] for x in socket.getaddrinfo(socket.gethostname(), 
        80, socket.AF_INET)]).pop()