def lookup(cls, basenote):
    for c in cls.mro():
        if 'provider_registry' not in vars(c):
            continue
        if basenote in c.provider_registry:
            return c.provider_registry[basenote]
    raise LookupError(repr(basenote))