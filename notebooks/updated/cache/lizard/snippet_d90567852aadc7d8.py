def _make_cmap(colors, position=None, bit=False):
    bit_rgb = np.linspace(0, 1, 256)
    if position == None:
        position = np.linspace(0, 1, len(colors))
    elif len(position) != len(colors):
        sys.exit('position length must be the same as colors')
    elif position[0] != 0 or position[-1] != 1:
        sys.exit('position must start with 0 and end with 1')
    palette = [(i, (float(r), float(g), float(b), float(a))) for i, (r, g,
        b, a) in enumerate(colors)]
    cmap = Colormap(*palette)
    return cmap