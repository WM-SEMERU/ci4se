def from_content_type(cls, content_type):
    name = content_type
    options = {}
    if ';' in content_type:
        name, options_str = content_type.split(';', 1)
        for part in options_str.split(';'):
            part = part.strip()
            if '=' in part:
                key, value = part.split('=')
            else:
                key, value = part, None
            options[key] = value
    if name.endswith('+zlib'):
        options['compression'] = 'zlib'
        name = name[:-5]
    return cls(name, charset=options.get('charset', 'UTF-8'), compression=
        options.get('compression'))