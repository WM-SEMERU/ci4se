def get(self):
    return {k: v for k, v in list(self.options.items()) if k in self.
        _allowed_layout}