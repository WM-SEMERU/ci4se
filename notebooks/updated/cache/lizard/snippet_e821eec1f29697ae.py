def versions_from_archive(self):
    py_vers = versions_from_trove(self.classifiers)
    return [ver for ver in py_vers if ver != self.unsupported_version]