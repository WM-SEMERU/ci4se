def create_from_position(cls, skydir, config, **kwargs):
    coordsys = kwargs.pop('coordsys', 'CEL')
    roi = cls(config, skydir=skydir, coordsys=coordsys, **kwargs)
    return roi