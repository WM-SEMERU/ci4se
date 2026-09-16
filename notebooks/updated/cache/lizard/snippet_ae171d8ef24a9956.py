def change_directory(self, path, *args, **kwargs):
    previous_path = self.session_path()
    self.session_path(path)
    if os.path.isdir(self.full_path()) is False:
        self.session_path(previous_path)
        raise ValueError(
            'Unable to change directory. It does not exist or is not a directory'
            )