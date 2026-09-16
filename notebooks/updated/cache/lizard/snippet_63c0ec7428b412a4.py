def render_import_image(self, use_auth=None):
    phases = 'postbuild_plugins', 'exit_plugins'
    plugin = 'import_image'
    for phase in phases:
        if (self.spec.imagestream_name.value is None or self.spec.
            imagestream_url.value is None):
            logger.info(
                'removing %s from request, registry or repo url is not defined'
                , plugin)
            self.dj.remove_plugin(phase, plugin)
            continue
        if self.dj.dock_json_has_plugin_conf(phase, plugin):
            self.dj.dock_json_set_arg(phase, plugin, 'imagestream', self.
                spec.imagestream_name.value)
            self.dj.dock_json_set_arg(phase, plugin, 'docker_image_repo',
                self.spec.imagestream_url.value)
            self.dj.dock_json_set_arg(phase, plugin, 'url', self.spec.
                builder_openshift_url.value)
            self.dj.dock_json_set_arg(phase, plugin, 'build_json_dir', self
                .spec.builder_build_json_dir.value)
            use_auth = self.spec.use_auth.value
            if use_auth is not None:
                self.dj.dock_json_set_arg(phase, plugin, 'use_auth', use_auth)
            if self.spec.imagestream_insecure_registry.value:
                self.dj.dock_json_set_arg(phase, plugin,
                    'insecure_registry', True)