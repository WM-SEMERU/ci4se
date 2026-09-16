def slugify_filename(filename):
    name, ext = os.path.splitext(filename)
    slugified = get_slugified_name(name)
    return slugified + ext