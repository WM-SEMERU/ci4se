def set_namespace(namespace, attribute, namespace_splitter=NAMESPACE_SPLITTER):
    long_name = '{0}{1}{2}'.format(namespace, namespace_splitter, attribute)
    LOGGER.debug("> Namespace: '{0}', attribute: '{1}', long name: '{2}'.".
        format(namespace, attribute, long_name))
    return long_name