def set_color_codes(palette='accent'):
    if palette not in PALETTES:
        raise YellowbrickValueError("'{}' is not a recognized palette!".
            format(palette))
    colors = PALETTES[palette]
    if len(colors) > 7:
        colors = colors[:7]
    elif len(colors) < 7:
        colors = colors + [YB_KEY]
    for code, color in zip('bgrmyck', colors):
        rgb = mpl.colors.colorConverter.to_rgb(color)
        mpl.colors.colorConverter.colors[code] = rgb
        mpl.colors.colorConverter.cache[code] = rgb