def format_requirement(ireq):
    if ireq.editable:
        line = '-e {}'.format(ireq.link)
    else:
        line = _requirement_to_str_lowercase_name(ireq.req)
    if str(ireq.req.marker) != str(ireq.markers):
        if not ireq.req.marker:
            line = '{}; {}'.format(line, ireq.markers)
        else:
            name, markers = line.split(';', 1)
            markers = markers.strip()
            line = '{}; ({}) and ({})'.format(name, markers, ireq.markers)
    return line