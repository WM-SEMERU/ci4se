def _unparse_changetype(self, mod_len):
    if mod_len == 2:
        changetype = 'add'
    elif mod_len == 3:
        changetype = 'modify'
    else:
        raise ValueError('modlist item of wrong length')
    self._unparse_attr('changetype', changetype)