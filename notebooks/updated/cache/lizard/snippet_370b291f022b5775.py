def _func_args_from_dict(self, d):
    filtered_d = self.filter_out_none_valued_keys(d)
    return ', '.join([('%s=%s' % (k, v)) for k, v in filtered_d.items()])