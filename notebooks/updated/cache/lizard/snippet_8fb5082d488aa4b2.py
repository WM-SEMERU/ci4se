def unregisterAddon(cls, name):
    prop = '_{0}__addons'.format(cls.__name__)
    cmds = getattr(cls, prop, {})
    cmds.pop(name, None)