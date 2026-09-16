def _import_class(self, class_path):
    LOGGER.debug('Importing %s', class_path)
    try:
        return utils.import_namespaced_class(class_path)
    except ImportError as error:
        LOGGER.critical('Could not import %s: %s', class_path, error)
        return None