def info(self):
    info = []
    name = self.__class__.__name__.lower()
    for key in VALID_BG_KEYS:
        if key in self.h5['bg_data']:
            attrs = self.h5['bg_data'][key].attrs
            for akey in attrs:
                atr = attrs[akey]
                var = '{} background {}'.format(name, akey)
                info.append((var, atr))
    if 'fit' in self.h5['bg_data']:
        var_mask = '{} background from mask'.format(name)
        if 'estimate_bg_from_mask' in self.h5 and self.h5[
            'estimate_bg_from_mask'] is not None:
            info.append((var_mask, True))
        elif 'estimate_bg_from_binary' in self.h5 and self.h5[
            'estimate_bg_from_binary'] is not None:
            warnings.warn('Old file format detected!', DeprecationWarning)
            info.append((var_mask, True))
        else:
            info.append((var_mask, False))
    return info