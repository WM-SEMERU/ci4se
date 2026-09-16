def scan(self, module, onerror=None, ignore=None):
    from venusian import Scanner
    scanner = Scanner(registry=self)
    kwargs = {'onerror': onerror, 'categories': ['method']}
    if ignore is not None:
        kwargs['ignore'] = ignore
    scanner.scan(module, **kwargs)