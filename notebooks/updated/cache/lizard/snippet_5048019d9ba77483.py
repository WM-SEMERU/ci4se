def _dict_to_html_attributes(d):
    if d is None:
        return ''
    return ''.join(' {}="{}"'.format(key, value) for key, value in iter(d.
        items()))