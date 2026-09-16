def smart_colormap(vmin, vmax, color_high='#b11902', hue_low=0.6):
    orig_cmap = matplotlib.colors.LinearSegmentedColormap.from_list('test',
        ['#FFFFFF', color_high], N=2048)
    vmin = float(vmin)
    vmax = float(vmax)
    mx = max([vmin, vmax])
    mn = min([vmin, vmax])
    frac = abs(mn / mx)
    rgb = orig_cmap(frac)[:-1]
    hsv = list(colorsys.rgb_to_hsv(*rgb))
    hsv[0] = hue_low
    new_rgb = colorsys.hsv_to_rgb(*hsv)
    new_hex = matplotlib.colors.rgb2hex(new_rgb)
    zeropoint = abs(-vmin / (vmax - vmin))
    new_cmap = matplotlib.colors.LinearSegmentedColormap.from_list('test',
        [(0, new_rgb), (zeropoint, '#FFFFFF'), (1, color_high)], N=2048)
    return new_cmap