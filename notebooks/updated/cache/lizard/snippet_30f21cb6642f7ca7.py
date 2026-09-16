def _GenerateInitConfigs(self, template_dir, rpm_build_dir):
    client_name = config.CONFIG.Get('Client.name', context=self.context)
    initd_target_filename = os.path.join(rpm_build_dir, 'etc/init.d',
        client_name)
    utils.EnsureDirExists(os.path.dirname(initd_target_filename))
    self.GenerateFile(os.path.join(template_dir,
        'rpmbuild/grr-client.initd.in'), initd_target_filename)
    if config.CONFIG['Template.version_numeric'] >= 3125:
        systemd_target_filename = os.path.join(rpm_build_dir,
            'usr/lib/systemd/system/', '%s.service' % client_name)
        utils.EnsureDirExists(os.path.dirname(systemd_target_filename))
        self.GenerateFile(os.path.join(template_dir,
            'rpmbuild/grr-client.service.in'), systemd_target_filename)