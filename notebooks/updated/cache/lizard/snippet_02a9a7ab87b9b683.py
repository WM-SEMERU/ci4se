def _check_type_and_load_cert(self, msg, key_type, cert_type):
    key_types = key_type
    cert_types = cert_type
    if isinstance(key_type, string_types):
        key_types = [key_types]
    if isinstance(cert_types, string_types):
        cert_types = [cert_types]
    if msg is None:
        raise SSHException('Key object may not be empty')
    msg.rewind()
    type_ = msg.get_text()
    if type_ in key_types:
        pass
    elif type_ in cert_types:
        self.load_certificate(Message(msg.asbytes()))
        msg.get_string()
    else:
        err = 'Invalid key (class: {}, data type: {}'
        raise SSHException(err.format(self.__class__.__name__, type_))