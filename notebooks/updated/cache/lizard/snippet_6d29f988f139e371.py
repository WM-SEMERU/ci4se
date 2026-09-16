def get_setting(self, key, default):
    gkey = 'ensime_{}'.format(key)
    return self._vim.vars.get(gkey, default)