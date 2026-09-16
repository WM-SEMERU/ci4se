def opensignals_kwargs(obj):
    out = None
    if obj == 'figure':
        out = {}
    elif obj == 'gridplot':
        out = {'toolbar_options': {'logo': None}, 'sizing_mode': 'scale_width'}
    elif obj == 'line':
        out = {'line_width': 2, 'line_color': opensignals_color_pallet()}
    return out