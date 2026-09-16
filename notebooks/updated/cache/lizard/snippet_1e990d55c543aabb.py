def is_enabled(self, cls):
    if cls not in self.enabled:
        self.enabled[cls] = self.is_component_enabled(cls)
    return self.enabled[cls]