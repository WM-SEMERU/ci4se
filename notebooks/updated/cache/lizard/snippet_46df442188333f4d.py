def get_colorscale(cmap, levels=None, cmin=None, cmax=None):
    ncolors = levels if isinstance(levels, int) else None
    if isinstance(levels, list):
        ncolors = len(levels) - 1
        if isinstance(cmap, list) and len(cmap) != ncolors:
            raise ValueError(
                'The number of colors in the colormap must match the intervals defined in the color_levels, expected %d colors found %d.'
                 % (ncolors, len(cmap)))
    try:
        palette = process_cmap(cmap, ncolors)
    except Exception as e:
        colorscale = colors.PLOTLY_SCALES.get(cmap)
        if colorscale is None:
            raise e
        return colorscale
    if isinstance(levels, int):
        colorscale = []
        scale = np.linspace(0, 1, levels + 1)
        for i in range(levels + 1):
            if i == 0:
                colorscale.append((scale[0], palette[i]))
            elif i == levels:
                colorscale.append((scale[-1], palette[-1]))
            else:
                colorscale.append((scale[i], palette[i - 1]))
                colorscale.append((scale[i], palette[i]))
        return colorscale
    elif isinstance(levels, list):
        palette, (cmin, cmax) = color_intervals(palette, levels, clip=(cmin,
            cmax))
    return colors.make_colorscale(palette)