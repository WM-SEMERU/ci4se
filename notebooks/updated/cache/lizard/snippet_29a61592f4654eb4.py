def db(self):
    if self._db is None:
        if self.tcex.default_args.tc_playbook_db_type == 'Redis':
            from .tcex_redis import TcExRedis
            self._db = TcExRedis(self.tcex.default_args.tc_playbook_db_path,
                self.tcex.default_args.tc_playbook_db_port, self.tcex.
                default_args.tc_playbook_db_context)
        elif self.tcex.default_args.tc_playbook_db_type == 'TCKeyValueAPI':
            from .tcex_key_value import TcExKeyValue
            self._db = TcExKeyValue(self.tcex)
        else:
            err = 'Invalid DB Type: ({})'.format(self.tcex.default_args.
                tc_playbook_db_type)
            raise RuntimeError(err)
    return self._db