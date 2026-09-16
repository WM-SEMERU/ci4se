def add_curves_from_lasio(self, l, remap=None, funcs=None):
    params = {}
    for field, (sect, code) in LAS_FIELDS['data'].items():
        params[field] = utils.lasio_get(l, sect, code, remap=remap, funcs=funcs
            )
    curves = {c.mnemonic: Curve.from_lasio_curve(c, **params) for c in l.curves
        }
    self.data.update(curves)
    return None