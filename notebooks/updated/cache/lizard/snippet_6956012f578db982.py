def delete_types(self, base_key, out_key, *types):
    self.params['%s.%s' % (base_key, out_key)] = self.delete_types_s(self.
        params[base_key], types)