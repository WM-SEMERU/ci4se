def load_requirements(self):
    for module_name, pip_name in iteritems(self.metadata.requirements):
        extant = self.dataset.config.requirements[module_name].url
        force = extant and extant != pip_name
        self._library.install_packages(module_name, pip_name, force=force)
        self.dataset.config.requirements[module_name].url = pip_name
    python_dir = self._library.filesystem.python()
    sys.path.append(python_dir)