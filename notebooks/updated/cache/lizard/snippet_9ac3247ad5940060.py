def get_color_palette(scheme):
    color_schemes = {'default': {'frames': ['tomato', 'limegreen',
        'deepskyblue'], 'background': '#ffffff', 'color': '#616161',
        'ticks': '#757575', 'start': '#ffffff', 'stop': '#909090', 'rna':
        '#eaeaea', 'axis': '#e0e0e0', 'grey': '#bdbdbd'}, 'colorbrewer': {
        'frames': ['#fc8d62', '#66c2a5', '#8da0cb']}, 'rgb': {'frames': [
        'red', 'green', 'blue']}, 'greyorfs': {}}
    colors = {}
    for k, v in color_schemes['default'].items():
        try:
            vals = color_schemes[scheme][k]
        except KeyError:
            vals = v
        colors[k] = vals
    return colors