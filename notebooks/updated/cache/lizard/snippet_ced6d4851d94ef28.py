def parse_image_spec(spec):
    match = re.match('(.+)\\s+\\"(.*)\\"\\s*$', spec)
    if match:
        spec, title = match.group(1, 2)
    else:
        title = None
    match = re.match('([^\\{]*)(\\{(.*)\\})\\s*$', spec)
    if match:
        spec = match.group(1)
        args = parse_arglist(match.group(3))
    else:
        args = {}
    return spec, args, title and html.unescape(title)