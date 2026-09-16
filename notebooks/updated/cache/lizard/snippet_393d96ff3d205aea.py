def _mpl_cmap2pgf_cmap(cmap, data):
    if isinstance(cmap, mpl.colors.LinearSegmentedColormap):
        return _handle_linear_segmented_color_map(cmap, data)
    assert isinstance(cmap, mpl.colors.ListedColormap
        ), 'Only LinearSegmentedColormap and ListedColormap are supported'
    return _handle_listed_color_map(cmap, data)