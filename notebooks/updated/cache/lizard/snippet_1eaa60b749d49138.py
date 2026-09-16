def handleHeader(self, key, value):
    if key == 'CIMError':
        self.CIMError = urllib.parse.unquote(value)
    if key == 'PGErrorDetail':
        self.PGErrorDetail = urllib.parse.unquote(value)