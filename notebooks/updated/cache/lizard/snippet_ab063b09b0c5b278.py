def to_str(self, pretty_print=False, encoding=None, **kw):
    u
    if kw.get('without_comments') and not kw.get('method'):
        kw.pop('without_comments')
        kw['method'] = 'c14n'
        kw['with_comments'] = False
    return etree.tostring(self._xml, pretty_print=pretty_print, encoding=
        encoding, **kw)