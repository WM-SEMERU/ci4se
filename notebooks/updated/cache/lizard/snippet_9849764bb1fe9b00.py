def update(self, cache):
    self.cache['delims'] = cache.get('delims')
    self.cache['opts'].update(cache.get('opts'))
    self.cache['rset'].update(cache.get('rset'))
    self.cache['mix'].update(cache.get('mix'))
    map(self.set_var, cache['ctx'].values())