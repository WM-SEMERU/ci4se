def toXml(cls, data, xparent=None):
    if data is None:
        return None
    if isinstance(data, XmlObject):
        name = 'object'
    else:
        name = type(data).__name__
    addon = cls.byName(name)
    if not addon:
        raise RuntimeError('{0} is not a supported XML tag'.format(name))
    return addon.save(data, xparent)