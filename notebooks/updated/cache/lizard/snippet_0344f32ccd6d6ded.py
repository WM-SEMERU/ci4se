def create_plot_option_dicts(info, marker_types=None, colors=None,
    line_dash=None, size=None):
    logging.debug('    - creating plot-options-dict (for bokeh)')
    if marker_types is None:
        marker_types = ['circle', 'square', 'triangle', 'invertedtriangle',
            'diamond', 'cross', 'asterix']
    if line_dash is None:
        line_dash = [0, 0]
    if size is None:
        size = 10
    groups = info.groups.unique()
    number_of_groups = len(groups)
    if colors is None:
        if number_of_groups < 4:
            colors = bokeh.palettes.brewer['YlGnBu'][3]
        else:
            colors = bokeh.palettes.brewer['YlGnBu'][min(9, number_of_groups)]
    sub_groups = info.sub_groups.unique()
    marker_it = itertools.cycle(marker_types)
    colors_it = itertools.cycle(colors)
    group_styles = dict()
    sub_group_styles = dict()
    for j in groups:
        color = next(colors_it)
        marker_options = {'line_color': color, 'fill_color': color}
        line_options = {'line_color': color}
        group_styles[j] = {'marker': marker_options, 'line': line_options}
    for j in sub_groups:
        marker_type = next(marker_it)
        marker_options = {'marker': marker_type, 'size': size}
        line_options = {'line_dash': line_dash}
        sub_group_styles[j] = {'marker': marker_options, 'line': line_options}
    return group_styles, sub_group_styles