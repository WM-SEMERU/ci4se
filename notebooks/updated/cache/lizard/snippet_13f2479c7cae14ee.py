def make_parameter_dict(pdict, fixed_par=False, rescale=True, update_bounds
    =False):
    o = copy.deepcopy(pdict)
    o.setdefault('scale', 1.0)
    if rescale:
        value, scale = utils.scale_parameter(o['value'] * o['scale'])
        o['value'] = np.abs(value) * np.sign(o['value'])
        o['scale'] = np.abs(scale) * np.sign(o['scale'])
        if 'error' in o:
            o['error'] /= np.abs(scale)
    if update_bounds:
        o['min'] = o['value'] * 0.001
        o['max'] = o['value'] * 1000.0
    if fixed_par:
        o['min'] = o['value']
        o['max'] = o['value']
    if float(o['min']) > float(o['value']):
        o['min'] = o['value']
    if float(o['max']) < float(o['value']):
        o['max'] = o['value']
    return o