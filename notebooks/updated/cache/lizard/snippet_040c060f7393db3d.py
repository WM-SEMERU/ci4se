def validate(self, value):
    if '.' not in value:
        self.error_message = '%s is not a fully qualified domain name.' % value
        return False
    try:
        ipaddress = socket.gethostbyname(value)
    except socket.gaierror:
        self.error_message = '%s does not resolve.' % value
        return False
    try:
        socket.gethostbyaddr(ipaddress)
    except socket.herror:
        self.error_message = '%s reverse address (%s) does not resolve.' % (
            value, ipaddress)
        return False
    self._choice = value
    return True