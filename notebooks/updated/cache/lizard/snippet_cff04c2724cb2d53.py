def split_uri(uri, mod_attr_sep='::'):
    uri_parts = uri.split(mod_attr_sep, 1)
    if len(uri_parts) == 2:
        mod_uri, attr_chain = uri_parts
    else:
        mod_uri = uri_parts[0]
        attr_chain = None
    if mod_uri.startswith('py://'):
        protocol = 'py'
        mod_uri = mod_uri[5:]
    elif mod_uri.startswith('file://'):
        protocol = 'file'
        mod_uri = mod_uri[7:]
    elif mod_uri.endswith('.py'):
        protocol = 'file'
    else:
        protocol = 'py'
    info = protocol, mod_uri, attr_chain
    return info