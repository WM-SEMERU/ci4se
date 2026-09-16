def _build_xpath_expr(attrs):
    if 'class_' in attrs:
        attrs['class'] = attrs.pop('class_')
    s = ['@{key}={val!r}'.format(key=k, val=v) for k, v in attrs.items()]
    return '[{expr}]'.format(expr=' and '.join(s))