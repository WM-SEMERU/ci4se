def disable_by_count(self):
    if self.enable_count > 0:
        self.enable_count -= 1
        if self.enable_count == 0:
            self.disable()