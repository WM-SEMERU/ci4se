def text(self):
    params = ', '.join(x.text for x in self.params)
    return '{0} ({1})'.format(self.proto_text, params)