def set_file(self, file=None, is_modified=False, is_untitled=False):
    LOGGER.debug("> Setting '{0}' editor file.".format(file))
    self.__file = file
    self.__is_untitled = is_untitled
    self.set_modified(is_modified)
    self.set_title()
    return True