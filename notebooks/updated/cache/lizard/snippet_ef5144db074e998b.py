def _safe_attr(attr, camel_killer=False, replacement_char='x'):
    allowed = string.ascii_letters + string.digits + '_'
    attr = _safe_key(attr)
    if camel_killer:
        attr = _camel_killer(attr)
    attr = attr.replace(' ', '_')
    out = ''
    for character in attr:
        out += character if character in allowed else '_'
    out = out.strip('_')
    try:
        int(out[0])
    except (ValueError, IndexError):
        pass
    else:
        out = '{0}{1}'.format(replacement_char, out)
    if out in kwlist:
        out = '{0}{1}'.format(replacement_char, out)
    return re.sub('_+', '_', out)