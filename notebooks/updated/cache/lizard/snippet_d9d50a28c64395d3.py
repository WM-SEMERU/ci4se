def remove_directories(self, directories):
    directories = util.to_absolute_paths(directories)
    self.plugin_directories = util.remove_from_set(self.plugin_directories,
        directories)