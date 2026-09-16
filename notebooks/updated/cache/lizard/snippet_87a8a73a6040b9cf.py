def fix_style(style='basic', ax=None, **kwargs):
    style = _read_style(style)
    for s in style:
        if not s in style_params.keys():
            avail = [f.replace('.mplstyle', '') for f in os.listdir(
                _get_lib()) if f.endswith('.mplstyle')]
            raise ValueError('{0} is not a valid style. '.format(s) +
                'Please pick a style from the list available in ' +
                '{0}: {1}'.format(_get_lib(), avail))
    _fix_style(style, ax, **kwargs)