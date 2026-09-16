def get_cmap(cmap=None):
    if isinstance(cmap, matplotlib.colors.Colormap):
        return cmap
    if isinstance(cmap, str):
        cmap_name = cmap
    else:
        cmap_name = DEFAULT_COLOR_MAP_NAME
    return plt.get_cmap(cmap_name)