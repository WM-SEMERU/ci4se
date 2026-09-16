def format_meta_lines(cls, meta, labels, offset, **kwargs):
    lines = []
    name = meta['package_name']
    if 'version' in meta:
        name += '-' + meta['version']
    if 'custom_location' in kwargs:
        name += ' ({loc})'.format(loc=kwargs['custom_location'])
    lines.append(name)
    lines.append(len(name) * '=')
    lines.append('')
    lines.extend(meta['summary'].splitlines())
    lines.append('')
    if meta.get('description', ''):
        lines.extend(meta['description'].splitlines())
        lines.append('')
    data = []
    for item in labels:
        if meta.get(item, '') != '':
            label = (cls._nice_strings[item] + ':').ljust(offset + 2)
            data.append(label + cls._format_field(meta[item]))
    lines.extend(data)
    return lines