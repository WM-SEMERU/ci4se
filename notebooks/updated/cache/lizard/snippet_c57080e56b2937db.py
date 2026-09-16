def is_active(self):
    if not self._multiplexer:
        return False
    scalars_plugin_instance = self._get_scalars_plugin()
    if not (scalars_plugin_instance and scalars_plugin_instance.is_active()):
        return False
    return bool(self._multiplexer.PluginRunToTagToContent(metadata.PLUGIN_NAME)
        )