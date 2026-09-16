def attribute_exists(self, attribute, section):
    if foundations.namespace.remove_namespace(attribute, root_only=True
        ) in self.get_attributes(section, strip_namespaces=True):
        LOGGER.debug("> '{0}' attribute exists in '{1}' section.".format(
            attribute, section))
        return True
    else:
        LOGGER.debug("> '{0}' attribute doesn't exists in '{1}' section.".
            format(attribute, section))
        return False