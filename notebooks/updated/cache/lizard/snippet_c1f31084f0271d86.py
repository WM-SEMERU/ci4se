def add_blacklisted_directories(self, directories,
    remove_from_stored_directories=True):
    absolute_paths = util.to_absolute_paths(directories)
    self.blacklisted_directories.update(absolute_paths)
    if remove_from_stored_directories:
        plug_dirs = self.plugin_directories
        plug_dirs = util.remove_from_set(plug_dirs, directories)