def write_utf(self, s):
    utfstr = s.encode('utf-8')
    length = len(utfstr)
    if length > 64:
        raise NamePartTooLongException
    self.write_byte(length)
    self.write_string(utfstr, length)