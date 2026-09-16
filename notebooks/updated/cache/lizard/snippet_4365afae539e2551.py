def set_style(style=None, rc=None):
    style_object = _axes_style(style, rc)
    mpl.rcParams.update(style_object)