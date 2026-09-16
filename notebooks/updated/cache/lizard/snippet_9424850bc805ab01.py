def __starttls(self, keyfile=None, certfile=None):
    if not self.has_tls_support():
        raise Error('STARTTLS not supported by the server')
    code, data = self.__send_command('STARTTLS')
    if code != 'OK':
        return False
    try:
        nsock = ssl.wrap_socket(self.sock, keyfile, certfile)
    except ssl.SSLError as e:
        raise Error('SSL error: %s' % str(e))
    self.sock = nsock
    self.__capabilities = {}
    self.__get_capabilities()
    return True