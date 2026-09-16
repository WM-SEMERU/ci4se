def export_cmd_options(self, options_override=None, standalone=False):
    cmd_options = super(MongosServer, self).export_cmd_options(options_override
        =options_override)
    cluster = self.get_validate_cluster()
    cmd_options['configdb'] = cluster.get_config_db_address()
    return cmd_options