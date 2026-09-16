def _plot_prepare(self, components, units):
    if components is None:
        components = self.pos.components
    n_comps = len(components)
    if units is not None:
        if isinstance(units, u.UnitBase):
            units = [units] * n_comps
        elif len(units) != n_comps:
            raise ValueError(
                'You must specify a unit for each axis, or a single unit for all axes.'
                )
    labels = []
    x = []
    for i, name in enumerate(components):
        val = getattr(self, name)
        if units is not None:
            val = val.to(units[i])
            unit = units[i]
        else:
            unit = val.unit
        if val.unit != u.one:
            uu = unit.to_string(format='latex_inline')
            unit_str = ' [{}]'.format(uu)
        else:
            unit_str = ''
        if name.startswith('d_'):
            dot = True
            name = name[2:]
        else:
            dot = False
        if name in _greek_letters:
            name = '\\{}'.format(name)
        if dot:
            name = '\\dot{{{}}}'.format(name)
        labels.append('${}$'.format(name) + unit_str)
        x.append(val.value)
    return x, labels