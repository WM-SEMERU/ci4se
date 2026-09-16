def get_password(self, service, username):
    service = escape_for_ini(service)
    username = escape_for_ini(username)
    try:
        password_base64 = self.config.get(service, username).encode()
        password_encrypted = base64.decodestring(password_base64)
        password = self.decrypt(password_encrypted).decode('utf-8')
    except (configparser.NoOptionError, configparser.NoSectionError):
        password = None
    return password