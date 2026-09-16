def get_allowed_plugins(self, placeholder_slot):
    slot_config = appsettings.FLUENT_CONTENTS_PLACEHOLDER_CONFIG.get(
        placeholder_slot) or {}
    plugins = slot_config.get('plugins')
    if not plugins:
        return self.get_plugins()
    else:
        try:
            return self.get_plugins_by_name(*plugins)
        except PluginNotFound as e:
            raise PluginNotFound(str(e) +
                " Update the plugin list of the FLUENT_CONTENTS_PLACEHOLDER_CONFIG['{0}'] setting."
                .format(placeholder_slot))