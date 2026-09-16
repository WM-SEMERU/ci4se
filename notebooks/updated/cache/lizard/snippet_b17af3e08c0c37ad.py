def get_setup_install_args(self, pkgname, setup_py, develop=False):
    headers = self.base_paths['headers']
    headers = headers / 'python{0}'.format(self.python_version) / pkgname
    install_arg = 'install' if not develop else 'develop'
    return [self.python, '-u', '-c', SETUPTOOLS_SHIM % setup_py,
        install_arg, '--single-version-externally-managed',
        '--install-headers={0}'.format(self.base_paths['headers']),
        '--install-purelib={0}'.format(self.base_paths['purelib']),
        '--install-platlib={0}'.format(self.base_paths['platlib']),
        '--install-scripts={0}'.format(self.base_paths['scripts']),
        '--install-data={0}'.format(self.base_paths['data'])]