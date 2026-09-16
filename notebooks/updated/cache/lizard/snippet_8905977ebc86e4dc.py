def dump(self, fp, encoding=None, errors='strict'):
    close = False
    if isinstance(fp, basestring):
        fp = file(fp, 'w')
        close = True
    try:
        if encoding is not None:
            iterable = (x.encode(encoding, errors) for x in self)
        else:
            iterable = self
        if hasattr(fp, 'writelines'):
            fp.writelines(iterable)
        else:
            for item in iterable:
                fp.write(item)
    finally:
        if close:
            fp.close()