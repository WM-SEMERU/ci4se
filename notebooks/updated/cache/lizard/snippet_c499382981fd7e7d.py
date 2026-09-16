def format(self, attrs, args=None):
    if args is None:
        return attrs
    out = {}
    for key, val in attrs.items():
        mba = {'indexer': 'annual'}
        for k, v in args.items():
            if isinstance(v, six.string_types
                ) and v in self._attrs_mapping.get(key, {}).keys():
                mba[k] = '{{{}}}'.format(v)
            elif isinstance(v, dict):
                if v:
                    dk, dv = v.copy().popitem()
                    if dk == 'month':
                        dv = 'm{}'.format(dv)
                    mba[k] = '{{{}}}'.format(dv)
            else:
                mba[k] = int(v) if isinstance(v, float) and v % 1 == 0 else v
        out[key] = val.format(**mba).format(**self._attrs_mapping.get(key, {}))
    return out