def get_colormap(name='cfastie', format='pil'):
    cmap_file = os.path.join(os.path.dirname(__file__), 'cmap', '{0}.txt'.
        format(name))
    with open(cmap_file) as cmap:
        lines = cmap.read().splitlines()
        colormap = [list(map(int, line.split())) for line in lines if not
            line.startswith('#')][1:]
    cmap = list(np.array(colormap).flatten())
    if format.lower() == 'pil':
        return cmap
    elif format.lower() == 'gdal':
        return np.array(list(_chunks(cmap, 3)))
    else:
        raise Exception('Unsupported {} colormap format'.format(format))