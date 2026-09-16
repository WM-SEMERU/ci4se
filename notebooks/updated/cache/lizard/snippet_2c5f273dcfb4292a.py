def _remove_blacklisted(self, directories):
    directories = util.to_absolute_paths(directories)
    directories = util.remove_from_set(directories, self.
        blacklisted_directories)
    return directories