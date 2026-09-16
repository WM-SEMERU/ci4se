def get_resource_path(name, raise_exception=False):
    if not RuntimeGlobals.resources_directories:
        RuntimeGlobals.resources_directories.append(os.path.normpath(os.
            path.join(umbra.__path__[0], Constants.resources_directory)))
    for path in RuntimeGlobals.resources_directories:
        path = os.path.join(path, name)
        if foundations.common.path_exists(path):
            LOGGER.debug("> '{0}' resource path: '{1}'.".format(name, path))
            return path
    if raise_exception:
        raise umbra.exceptions.ResourceExistsError(
            "{0} | No resource file path found for '{1}' name!".format(
            __name__, name))