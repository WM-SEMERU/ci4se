def get_filename(file):
    if not os.path.exists(file):
        return None
    return '%s%s' % os.path.splitext(file)