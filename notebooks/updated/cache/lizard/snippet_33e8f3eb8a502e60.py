def accept_encoding(self):
    ret = ''
    accept_encoding = self.get_header('Accept-Charset', '')
    if accept_encoding:
        bits = re.split('\\s+', accept_encoding)
        bits = bits[0].split(';')
        ret = bits[0]
    return ret