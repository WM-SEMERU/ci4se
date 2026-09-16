def filter(self, value, model=None, context=None):
    value = str(value)
    linker = Linker(**self.linkify_params)
    return linker.linkify(value)