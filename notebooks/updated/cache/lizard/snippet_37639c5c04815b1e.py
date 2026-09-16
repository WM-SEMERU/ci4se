def startup_config_content(self, startup_config):
    try:
        startup_config_path = os.path.join(self.working_dir,
            'startup-config.cfg')
        if startup_config is None:
            startup_config = ''
        if len(startup_config) == 0 and os.path.exists(startup_config_path):
            return
        with open(startup_config_path, 'w+', encoding='utf-8') as f:
            if len(startup_config) == 0:
                f.write('')
            else:
                startup_config = startup_config.replace('%h', self._name)
                f.write(startup_config)
        vlan_file = os.path.join(self.working_dir, 'vlan.dat-{:05d}'.format
            (self.application_id))
        if os.path.exists(vlan_file):
            try:
                os.remove(vlan_file)
            except OSError as e:
                log.error("Could not delete VLAN file '{}': {}".format(
                    vlan_file, e))
    except OSError as e:
        raise IOUError("Can't write startup-config file '{}': {}".format(
            startup_config_path, e))