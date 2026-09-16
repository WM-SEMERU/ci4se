def set_global_fontsize_from_fig(fig, scale=1.5):
    fig_size_inch = fig.get_size_inches()
    fig_size_len_geom_mean = (fig_size_inch[0] * fig_size_inch[1]) ** 0.5
    rcParams['font.size'] = fig_size_len_geom_mean * scale
    return rcParams['font.size']