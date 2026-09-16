def _get_all_ns_packages(self):
    pkgs = self.distribution.namespace_packages or []
    return sorted(flatten(map(self._pkg_names, pkgs)))