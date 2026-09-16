def header(self, text, level):
    m = self.reWS.match(text)
    prefix = m.group(1)
    text = m.group(2)
    suffix = m.group(3)
    return '#' * level + ' %(text)s  \n' % locals()