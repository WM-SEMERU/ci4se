def GetAllPluginInformation(cls, show_all=True):
    results = []
    for plugin_class in iter(cls._plugin_classes.values()):
        plugin_object = plugin_class()
        if not show_all and not plugin_class.ENABLE_IN_EXTRACTION:
            continue
        doc_string, _, _ = plugin_class.__doc__.partition('\n')
        type_string = cls._PLUGIN_TYPE_STRINGS.get(plugin_object.plugin_type)
        information_tuple = plugin_object.plugin_name, doc_string, type_string
        results.append(information_tuple)
    return sorted(results)