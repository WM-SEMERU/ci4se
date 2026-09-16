def complete(self):
    if not self._techniques:
        return False
    if not any(tech._is_overriden('complete') for tech in self._techniques):
        return False
    return self.completion_mode(tech.complete(self) for tech in self.
        _techniques if tech._is_overriden('complete'))