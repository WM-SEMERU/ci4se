def install(cls, mbox):

    def wrap(fn):
        setattr(fn, cls.INSTALL_ATTRIBUTE, mbox)
        return fn
    return wrap