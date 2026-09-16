def load_default(self):
    appdir = AppDirs(self.application_name, self.application_author,
        version=self.application_version)
    file_name = os.path.join(appdir.site_data_dir, '{0}.conf'.format(self.
        application_name.lower()))
    if os.path.exists(file_name):
        self.load(file_name)
    if os.name is not 'posix' or os.getuid() > 0:
        config_file = os.path.join(appdir.user_data_dir, '{0}.conf'.format(
            self.application_name.lower()))
        if os.path.exists(config_file):
            self.load(config_file)