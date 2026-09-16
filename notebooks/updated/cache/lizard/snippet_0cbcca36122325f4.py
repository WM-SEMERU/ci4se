def is_python_binding_installed(self):
    is_installed = False
    is_install_error = False
    try:
        is_installed = self.is_python_binding_installed_on_pip()
    except InstallError:
        is_install_error = True
    if not is_installed or is_install_error:
        for rpm_dir in self.python_lib_rpm_dirs:
            init_py = os.path.join(rpm_dir, '__init__.py')
            if os.path.isfile(init_py):
                is_installed = True
                break
    return is_installed