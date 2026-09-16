def get_defaults():
    DEFAULTS = {}
    if 'PC_PIPE_BUF' in os.pathconf_names:
        x, y = os.pipe()
        DEFAULTS['PIPE_BUF'] = os.fpathconf(x, 'PC_PIPE_BUF')
    else:
        DEFAULTS['PIPE_BUF'] = 512
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    DEFAULTS['TCP_SNDBUF'] = tcp_sock.getsockopt(socket.SOL_SOCKET, socket.
        SO_SNDBUF)
    DEFAULTS['TCP_RCVBUF'] = tcp_sock.getsockopt(socket.SOL_SOCKET, socket.
        SO_RCVBUF)
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    DEFAULTS['UDP_SNDBUF'] = udp_sock.getsockopt(socket.SOL_SOCKET, socket.
        SO_SNDBUF)
    DEFAULTS['UDP_RCVBUF'] = udp_sock.getsockopt(socket.SOL_SOCKET, socket.
        SO_RCVBUF)
    DEFAULTS['WHATS_MYIP_URL'
        ] = 'http://www.whatismyip.com/automation/n09230945.asp'
    return DEFAULTS