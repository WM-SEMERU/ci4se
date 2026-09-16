def process_meta(cls, line, kwargs):
    if line.startswith('slug:'):
        kwargs['slug'] = line[5:].strip()
    elif line.startswith('public:'):
        try:
            kwargs['public'] = _str_to_bool(line[7:])
        except ValueError:
            LOG.warning('invalid boolean value for public', exc_info=True)
    elif line.startswith('private:'):
        try:
            kwargs['public'] = not _str_to_bool(line[8:])
        except ValueError:
            LOG.warning('invalid boolean value for private', exc_info=True)