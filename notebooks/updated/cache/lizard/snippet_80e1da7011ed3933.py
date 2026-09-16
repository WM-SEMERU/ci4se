def dependencies_satisfied(self, plugin):
    for depends in plugin.dependencies:
        if depends not in self.config['plugins']:
            log.error(
                "{0} depends on {1}, but {1} wasn't in the config file. To use {0}, install {1} and add it to the config."
                .format(plugin.name, depends))
            return False
    return True