def get_archive(self, archive_name):
    try:
        spec = self._get_archive_spec(archive_name)
        return spec
    except KeyError:
        raise KeyError('Archive "{}" not found'.format(archive_name))