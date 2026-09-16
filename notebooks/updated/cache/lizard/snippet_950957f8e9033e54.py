def parse_template(template):
    m = TEMPLATE_OVERRIDE_RE.match(template)
    if not m:
        return template, 0
    return m.group('template'), int(m.group('depth'))