def create_installer(self, rpm_py_version, **kwargs):
    return FedoraInstaller(rpm_py_version, self.python, self.rpm, **kwargs)