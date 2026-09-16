def resize(self, size, disk=None):
    if isinstance(size, Size):
        size = size.slug
    opts = {'disk': disk} if disk is not None else {}
    return self.act(type='resize', size=size, **opts)