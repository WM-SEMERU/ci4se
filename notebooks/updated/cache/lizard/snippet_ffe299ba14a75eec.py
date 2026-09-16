def _find_filepath_in_roots(filename):
    for root in settings.DJANGO_STATIC_MEDIA_ROOTS:
        filepath = _filename2filepath(filename, root)
        if os.path.isfile(filepath):
            return filepath, root
    if settings.DEBUG:
        try:
            from django.contrib.staticfiles import finders
            absolute_path = finders.find(filename)
            if absolute_path:
                root, filepath = os.path.split(absolute_path)
                return absolute_path, root
        except ImportError:
            pass
    return None, None