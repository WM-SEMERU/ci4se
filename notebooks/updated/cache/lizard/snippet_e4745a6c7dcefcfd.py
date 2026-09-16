def destroySingleton(cls):
    singleton_key = '_{0}__singleton'.format(cls.__name__)
    singleton = getattr(cls, singleton_key, None)
    if singleton is not None:
        setattr(cls, singleton_key, None)
        singleton.close()
        singleton.deleteLater()