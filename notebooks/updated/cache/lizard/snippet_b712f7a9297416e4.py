def component_by_key(self, key):
    filtered = [c for c in self.components if c.key == key]
    if filtered:
        return filtered[0]
    return None