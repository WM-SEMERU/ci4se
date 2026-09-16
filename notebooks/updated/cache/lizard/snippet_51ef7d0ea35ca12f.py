def write_lines(self, lines, encoding=None, errors='strict', linesep=os.
    linesep, append=False):
    r
    with self.open('ab' if append else 'wb') as f:
        for l in lines:
            isUnicode = isinstance(l, text_type)
            if linesep is not None:
                pattern = U_NL_END if isUnicode else NL_END
                l = pattern.sub('', l) + linesep
            if isUnicode:
                l = l.encode(encoding or sys.getdefaultencoding(), errors)
            f.write(l)