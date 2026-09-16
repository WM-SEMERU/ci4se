def render_check_and_set_platforms(self):
    phase = 'prebuild_plugins'
    plugin = 'check_and_set_platforms'
    if not self.pt.has_plugin_conf(phase, plugin):
        return
    if self.user_params.koji_target.value:
        self.pt.set_plugin_arg(phase, plugin, 'koji_target', self.
            user_params.koji_target.value)