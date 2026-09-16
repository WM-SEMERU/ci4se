def get_imports(self, option):
    if option:
        if len(option) == 1 and option[0].isupper() and len(option[0]) > 3:
            return getattr(settings, option[0])
        else:
            codes = [e for e in option if e.isupper() and len(e) == 3]
            if len(codes) != len(option):
                raise ImproperlyConfigured(
                    'Invalid currency codes found: %s' % codes)
            return codes
    for attr in ('CURRENCIES', 'SHOP_CURRENCIES'):
        try:
            return getattr(settings, attr)
        except AttributeError:
            continue
    return option