def default_value(self):
    if callable(self.default) and self.call_default:
        return self.default()
    return self.default