def list_basebackups(self, arg):
    self.config = config.read_json_config_file(arg.config, check_commands=
        False, check_pgdata=False)
    site = config.get_site_from_config(self.config, arg.site)
    self.storage = self._get_object_storage(site, pgdata=None)
    self.storage.show_basebackup_list(verbose=arg.verbose)