def setup(config):
    if config is None:
        config = {}
    else:
        config = config.copy()
    volume_cmd.CONF._ConfigOpts__cache = MyDict()
    storage = config.pop('storage', None) or DEFAULT_STORAGE
    if isinstance(storage, base.PersistenceDriverBase):
        return storage
    if inspect.isclass(storage) and issubclass(storage, base.
        PersistenceDriverBase):
        return storage(**config)
    if not isinstance(storage, six.string_types):
        raise exception.InvalidPersistence(storage)
    persistence_driver = driver.DriverManager(namespace=
        'cinderlib.persistence.storage', name=storage, invoke_on_load=True,
        invoke_kwds=config)
    return persistence_driver.driver