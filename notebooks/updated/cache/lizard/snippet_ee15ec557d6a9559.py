def to_dict(potential):
    from .. import potential as gp
    if isinstance(potential, gp.CompositePotential):
        d = dict()
        d['class'] = potential.__class__.__name__
        d['components'] = []
        for k, p in potential.items():
            comp_dict = _to_dict_help(p)
            comp_dict['name'] = k
            d['components'].append(comp_dict)
        if (potential.__class__.__name__ == 'CompositePotential' or 
            potential.__class__.__name__ == 'CCompositePotential'):
            d['type'] = 'composite'
        else:
            d['type'] = 'custom'
    else:
        d = _to_dict_help(potential)
    return d