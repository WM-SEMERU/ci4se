def get_info(self):
    plugin_infos = {}
    for pc in self.plugins:
        plugin_infos.update(pc.get_info())
    return {self.get_plugin_name(): {'version': self.get_version(),
        'sub-plugins': plugin_infos, 'params': {'multi_plugins': self.conf[
        'multi_plugins']}}}