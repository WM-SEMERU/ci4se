def isconfigurabletype(mixed, *, strict=False):
    from bonobo.config.configurables import ConfigurableMeta, PartiallyConfigured
    if isinstance(mixed, ConfigurableMeta):
        return True
    if strict:
        return False
    if isinstance(mixed, PartiallyConfigured):
        return True
    if hasattr(mixed, '_partial') and mixed._partial:
        return True
    return False