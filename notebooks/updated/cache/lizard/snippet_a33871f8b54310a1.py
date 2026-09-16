def genomic_signal(fn, kind):
    try:
        klass = _registry[kind.lower()]
    except KeyError:
        raise ValueError('No support for %s format, choices are %s' % (kind,
            _registry.keys()))
    m = klass(fn)
    m.kind = kind
    return m