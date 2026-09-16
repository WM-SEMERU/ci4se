def build_css_class(localized_fieldname, prefix=''):
    bits = localized_fieldname.split('_')
    css_class = ''
    if len(bits) == 1:
        css_class = str(localized_fieldname)
    elif len(bits) == 2:
        css_class = '-'.join(bits)
    elif len(bits) > 2:
        css_class = _join_css_class(bits, 2)
        if not css_class:
            css_class = _join_css_class(bits, 1)
    return '%s-%s' % (prefix, css_class) if prefix else css_class