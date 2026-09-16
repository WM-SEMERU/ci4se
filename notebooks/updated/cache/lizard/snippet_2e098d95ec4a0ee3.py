def load_creds_file(self, path, profile=None):
    config_cls = self.get_creds_reader()
    return config_cls.load_config(self, path, profile=profile)