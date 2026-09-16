def install_local(self):
    folder = self._get_local_folder()
    installed = self.installed_dir()
    self._check_module(installed.parent)
    installed.symlink_to(folder.resolve())