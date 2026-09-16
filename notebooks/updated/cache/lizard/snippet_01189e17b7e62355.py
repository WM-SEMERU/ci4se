def colorMap(value, name='jet', vmin=None, vmax=None):
    if not _mapscales:
        print(
            '-------------------------------------------------------------------'
            )
        print(
            'WARNING : cannot import matplotlib.cm (colormaps will show up gray).'
            )
        print('Try e.g.: sudo apt-get install python3-matplotlib')
        print('     or : pip install matplotlib')
        print(
            '     or : build your own map (see example in basic/mesh_custom.py).'
            )
        return 0.5, 0.5, 0.5
    if isinstance(name, matplotlib.colors.LinearSegmentedColormap):
        mp = name
    elif name in _mapscales.keys():
        mp = _mapscales[name]
    else:
        print('Error in colorMap():', name, '\navaliable maps =', sorted(
            _mapscales.keys()))
        exit(0)
    if _isSequence(value):
        values = np.array(value)
        if vmin is None:
            vmin = np.min(values)
        if vmax is None:
            vmax = np.max(values)
        values = np.clip(values, vmin, vmax)
        values -= vmin
        values /= vmax - vmin
        cols = []
        mp = _mapscales[name]
        for v in values:
            cols.append(mp(v)[0:3])
        return np.array(cols)
    else:
        value -= vmin
        value /= vmax - vmin
        if value > 0.999:
            value = 0.999
        elif value < 0:
            value = 0
        return mp(value)[0:3]