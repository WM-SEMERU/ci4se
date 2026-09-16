def dict_key(self):
    while True:
        token = self.next()
        t_value = token['value']
        if t_value == '\n':
            continue
        if t_value == '}':
            raise self.ParseEnd()
        if token['type'] == 'literal':
            return self.make_value(t_value)
        self.error('Invalid Key')