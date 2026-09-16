def LoadPlugins(cls):
    if cls.PLUGINS_LOADED:
        return
    reg = ComponentRegistry()
    for _, record in reg.load_extensions('iotile.update_record'):
        cls.RegisterRecordType(record)
    cls.PLUGINS_LOADED = True