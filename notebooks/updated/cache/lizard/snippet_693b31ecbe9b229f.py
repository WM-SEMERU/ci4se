def icon_resource(name, package=None):
    if not package:
        package = '%s.resources.images' % calling_package()
    name = resource_filename(package, name)
    if not name.startswith('/'):
        return 'file://%s' % abspath(name)
    return 'file://%s' % name