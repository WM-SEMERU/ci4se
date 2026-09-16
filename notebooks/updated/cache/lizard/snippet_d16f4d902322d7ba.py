def get_plugin(self, plugin_type, name, version=None):
    if not self.loaded:
        self.load_modules()
    return get_plugins()[self.group]._filter(blacklist=self.blacklist,
        newest_only=True, type_filter=self.type_filter, type=plugin_type,
        name=name, version=version)