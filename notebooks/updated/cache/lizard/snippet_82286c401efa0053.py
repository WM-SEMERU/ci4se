def resolve_context(self, verbosity=0, max_fails=-1, timestamp=None,
    callback=None, buf=None, package_load_callback=None):
    package_filter = PackageFilterList.from_pod(self.package_filter)
    context = ResolvedContext(self.request, package_paths=self.
        packages_path, package_filter=package_filter, verbosity=verbosity,
        max_fails=max_fails, timestamp=timestamp, buf=buf, callback=
        callback, package_load_callback=package_load_callback, caching=self
        .caching)
    if context.success:
        if self._context and self._context.load_path:
            context.set_load_path(self._context.load_path)
        self._set_context(context)
        self._modified = True
    return context