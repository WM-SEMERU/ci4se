def _generateAlias(self):
    for i in range(1000):
        alias = 'cust%d' % (i,)
        if alias not in self.auth_level_aliases:
            return alias
    raise RuntimeError('Could not find an unused alias (tried 1000!)')