def _get_ticks(data, xy, ticks, ticklabels):
    axis_options = []
    pgfplots_ticks = []
    pgfplots_ticklabels = []
    is_label_required = False
    for tick, ticklabel in zip(ticks, ticklabels):
        pgfplots_ticks.append(tick)
        label = ticklabel.get_text()
        if ticklabel.get_visible():
            label = mpl_backend_pgf.common_texification(label)
            pgfplots_ticklabels.append(label)
        else:
            is_label_required = True
        if label:
            try:
                label_float = float(label.replace('−', '-'))
                is_label_required = (is_label_required or label and 
                    label_float != tick)
            except ValueError:
                is_label_required = True
    if data['strict'] or is_label_required:
        if pgfplots_ticks:
            ff = data['float format']
            axis_options.append('{}tick={{{}}}'.format(xy, ','.join([ff.
                format(el) for el in pgfplots_ticks])))
        else:
            val = '{}' if 'minor' in xy else '\\empty'
            axis_options.append('{}tick={}'.format(xy, val))
        if is_label_required:
            axis_options.append('{}ticklabels={{{}}}'.format(xy, ','.join(
                pgfplots_ticklabels)))
    return axis_options