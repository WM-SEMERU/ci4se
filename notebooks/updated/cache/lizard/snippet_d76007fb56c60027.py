def backend_inst_from_mod(mod, encoding, encoding_errors, kwargs):
    kw = dict(encoding=encoding, encoding_errors=encoding_errors, kwargs=kwargs
        )
    try:
        klass = getattr(mod, 'Backend')
    except AttributeError:
        raise AttributeError('%r mod does not define any backend class' % mod)
    inst = klass(**kw)
    try:
        inst.check(title=False)
    except Exception as err:
        bin_mod = 'fulltext.backends.__bin'
        warn("can't use %r due to %r; use %r backend instead" % (mod, str(
            err), bin_mod))
        inst = import_mod(bin_mod).Backend(**kw)
        inst.check(title=False)
    LOGGER.debug('using %r' % inst)
    return inst