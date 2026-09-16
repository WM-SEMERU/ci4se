def hist(hist_function, *, options={}, **interact_params):
    params = {'marks': [{'sample': _array_or_placeholder(hist_function),
        'bins': _get_option('bins'), 'normalized': _get_option('normalized'
        ), 'scales': lambda opts: {'sample': opts['x_sc'], 'count': opts[
        'y_sc']}}]}
    fig = options.get('_fig', False) or _create_fig(options=options)
    [hist] = _create_marks(fig=fig, marks=[bq.Hist], options=options,
        params=params)
    _add_marks(fig, [hist])

    def wrapped(**interact_params):
        hist.sample = util.maybe_call(hist_function, interact_params)
    controls = widgets.interactive(wrapped, **interact_params)
    return widgets.VBox([controls, fig])