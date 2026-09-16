def _brute_force_install_pip(self):
    if os.path.exists(self.pip_installer_fname):
        logger.debug('Using pip installer from %r', self.pip_installer_fname)
    else:
        logger.debug('Installer for pip not found in %r, downloading it',
            self.pip_installer_fname)
        self._download_pip_installer()
    logger.debug('Installing PIP manually in the virtualenv')
    python_exe = os.path.join(self.env_bin_path, 'python')
    helpers.logged_exec([python_exe, self.pip_installer_fname, '-I'])
    self.pip_installed = True