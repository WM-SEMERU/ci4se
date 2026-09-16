def _scrub_method_name(self, method_name):
    if method_name not in self._scrubbed_method_names:
        self._scrubbed_method_names[method_name] = scrub_method_name(
            method_name)
    return self._scrubbed_method_names[method_name]