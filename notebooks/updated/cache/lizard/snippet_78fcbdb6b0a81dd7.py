def set(self, key, value):
    if not self.subsystem.is_cut:
        super().set(key, value)