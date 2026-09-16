def ul(self, text):
    m = self.reWS.match(text)
    ul = []
    for l in m.group(2).split('\n'):
        prefix, text, suffix = self._snip_whitespace(l)
        ul.append('%(prefix)s* %(text)s  ' % locals())
    return '\n'.join(ul) + '\n\n'