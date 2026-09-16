def normalize_linefeeds(self, a_string):
    newline = re.compile('(\r\r\r\n|\r\r\n|\r\n|\n\r)')
    a_string = newline.sub(self.RESPONSE_RETURN, a_string)
    if self.RESPONSE_RETURN == '\n':
        return re.sub('\r', self.RESPONSE_RETURN, a_string)