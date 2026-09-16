def make_tag(name, attrs, start_end=False):
    text = '<' + name
    if isinstance(attrs, dict):
        attr_list = attrs.items()
    elif isinstance(attrs, list):
        attr_list = attrs
    elif attrs is not None:
        raise TypeError('Unhandled attrs type ' + str(type(attrs)))
    for key, val in attr_list:
        if val is not None:
            escaped = html.escape(str(val), False).replace('"', '&#34;')
            text += ' {}="{}"'.format(key, escaped)
    if start_end:
        text += ' /'
    text += '>'
    return flask.Markup(text)