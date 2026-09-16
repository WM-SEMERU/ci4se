def get_content_type_charset(self, default='UTF-8'):
    encoding = default
    header = self.headers.get('Content-Type', '')
    idx = header.find('charset=')
    if idx > 0:
        encoding = header[idx + 8:].split(' ', 1)[0] or encoding
    return encoding