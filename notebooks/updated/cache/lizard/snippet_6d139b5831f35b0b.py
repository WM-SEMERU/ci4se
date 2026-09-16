def startup_config_path(self):
    return os.path.join(self._working_directory, 'configs',
        'i{}_startup-config.cfg'.format(self._dynamips_id))