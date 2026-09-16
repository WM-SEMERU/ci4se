def is_valid_ip(ip_address):
    valid = True
    try:
        socket.inet_aton(ip_address.strip())
    except:
        valid = False
    return valid