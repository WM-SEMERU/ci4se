def parse_k(self, k, vals):
    try:
        k = int(k)
    except:
        pass
    else:
        assert k in vals, 'k {0} not in vals'.format(k)
        return [k]
    if k is None:
        return vals
    else:
        try:
            k_vals = vals[k]
        except Exception as e:
            raise Exception('error slicing vals with {0}:{1}'.format(k, str(e))
                )
        return k_vals