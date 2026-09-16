def set_blacklisted_directories(self, directories,
    rm_black_dirs_from_stored_dirs=True):
    set_black_dirs = self.directory_manager.set_blacklisted_directories
    set_black_dirs(directories, rm_black_dirs_from_stored_dirs)