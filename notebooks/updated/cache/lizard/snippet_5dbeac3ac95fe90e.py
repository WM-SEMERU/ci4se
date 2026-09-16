def from_string(cls, contents, **kwargs):
    lines = contents.splitlines()
    title = None
    description = None
    line = lines.pop(0)
    while line != '':
        if not title and line.startswith('#'):
            title = line[1:].strip()
        elif line.startswith('title:'):
            title = line[6:].strip()
        elif line.startswith('description:'):
            description = line[12:].strip()
        elif line.startswith('subtitle:'):
            kwargs['subtitle'] = line[9:].strip()
        elif line.startswith('comments:'):
            try:
                kwargs['allow_comments'] = _str_to_bool(line[9:])
            except ValueError:
                LOG.warning('invalid boolean value for comments', exc_info=True
                    )
        cls.process_meta(line, kwargs)
        line = lines.pop(0)
    body = '\n'.join(lines).strip()
    excerpt = _get_excerpt(body)
    if description is None:
        description = _get_description(excerpt, 160)
    if issubclass(cls, Post):
        kwargs['excerpt'] = render_markdown(excerpt)
    body = render_markdown(body)
    return cls(title=title, body=body, description=description, **kwargs)