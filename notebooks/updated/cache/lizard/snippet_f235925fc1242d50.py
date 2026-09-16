def _update_cache(self):
    expected_version = tuple(r._version for r in self.registries) + (self.
        _extra_registry._version,)
    if self._last_version != expected_version:
        registry2 = Registry()
        for reg in self.registries:
            registry2.key_bindings.extend(reg.key_bindings)
        registry2.key_bindings.extend(self._extra_registry.key_bindings)
        self._registry2 = registry2
        self._last_version = expected_version