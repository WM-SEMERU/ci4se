def _exclude_pkg_path(self, pkg, exclusion_path):
    parts = pkg.split('.') + [exclusion_path]
    return os.path.join(self.install_dir, *parts)