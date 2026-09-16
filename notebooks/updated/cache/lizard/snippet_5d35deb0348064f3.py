def get_plugin_by_model(self, model_class):
    self._import_plugins()
    assert issubclass(model_class, ContentItem)
    try:
        name = self._name_for_model[model_class]
    except KeyError:
        raise PluginNotFound("No plugin found for model '{0}'.".format(
            model_class.__name__))
    return self.plugins[name]