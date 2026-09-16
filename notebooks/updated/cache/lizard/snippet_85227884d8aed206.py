def del_bg(self, key):
    if key not in VALID_BG_KEYS:
        raise ValueError('Invalid bg key: {}'.format(key))
    if key in self.h5['bg_data']:
        del self.h5['bg_data'][key]
    else:
        msg = "No bg data to clear for '{}' in {}.".format(key, self)
        warnings.warn(msg)