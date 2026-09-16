def restore_session(self):
    session = [foundations.strings.to_string(path) for path in self.
        __settings.get_key(self.__settings_section, 'session').toStringList
        () if foundations.common.path_exists(path)]
    LOGGER.debug("> Restoring session :'{0}'.".format(session))
    success = True
    for path in session:
        if os.path.isfile(path):
            success *= self.load_file(path)
        else:
            success *= self.add_project(path)
    return success