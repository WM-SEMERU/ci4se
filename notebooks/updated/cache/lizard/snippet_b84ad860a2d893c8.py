def modify_no_rollback(self, dn: str, mod_list: dict):
    _debug('modify_no_rollback', self, dn, mod_list)
    result = self._do_with_retry(lambda obj: obj.modify_s(dn, mod_list))
    _debug('--')
    return result