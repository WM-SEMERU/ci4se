def name(self):
    return ''.join('_%s' % c if c.isupper() else c for c in self.__class__.
        __name__).strip('_').lower()