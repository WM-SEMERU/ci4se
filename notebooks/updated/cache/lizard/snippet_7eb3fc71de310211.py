def get_account_config(self, id_or_name):
    if id_or_name in self._config:
        return self._config[id_or_name]
    if id_or_name in self._acct_name_to_id:
        return self._config[self._acct_name_to_id[id_or_name]]
    raise RuntimeError('ERROR: Unknown account ID or name')