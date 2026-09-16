def whois(ip_address):
    whois_ip = str(ip_address)
    try:
        query = socket.gethostbyname(whois_ip)
    except Exception:
        query = whois_ip
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('whois.ripe.net', 43))
    s.send(query.encode('utf8') + b'\r\n')
    answer = b''
    while True:
        d = s.recv(4096)
        answer += d
        if not d:
            break
    s.close()
    ignore_tag = b'remarks:'
    lines = [line for line in answer.split(b'\n') if not line or line and 
        not line.startswith(ignore_tag)]
    for i in range(1, len(lines)):
        if not lines[-i].strip():
            del lines[-i]
        else:
            break
    return b'\n'.join(lines[3:])