def open_resource(self, resource_name, access_mode=constants.AccessModes.
    no_lock, open_timeout=constants.VI_TMO_IMMEDIATE, resource_pyclass=None,
    **kwargs):
    if resource_pyclass is None:
        info = self.resource_info(resource_name, extended=True)
        try:
            resource_pyclass = self._resource_classes[info.interface_type,
                info.resource_class]
        except KeyError:
            resource_pyclass = self._resource_classes[constants.
                InterfaceType.unknown, '']
            logger.warning('There is no class defined for %r. Using Resource',
                (info.interface_type, info.resource_class))
    res = resource_pyclass(self, resource_name)
    for key in kwargs.keys():
        try:
            getattr(res, key)
            present = True
        except AttributeError:
            present = False
        except errors.InvalidSession:
            present = True
        if not present:
            raise ValueError('%r is not a valid attribute for type %s' % (
                key, res.__class__.__name__))
    res.open(access_mode, open_timeout)
    self._created_resources.add(res)
    for key, value in kwargs.items():
        setattr(res, key, value)
    return res