def should_register(self, app):
    if self.only_if is None:
        return True
    elif callable(self.only_if):
        return self.only_if(app)
    return bool(self.only_if)