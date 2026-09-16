def _set_filename(title, pelican_path):
    name = title.replace('/', '_').replace('\\', '_').replace(' ', '_'
        ).replace(':', '_').replace('&', '').replace('?', '').replace('!', '')
    return '{}/{}.html'.format(pelican_path, name)