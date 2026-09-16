def quote(self, data):
    if self.lang == 'python':
        quote_char = "'"
    elif self.lang == 'java':
        quote_char = "'"
    if re.findall('[!\\-\\=\\s\\$\\&]{1,}', str(data)):
        data = '{0}{1}{0}'.format(quote_char, data)
    return data