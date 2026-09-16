def get_alias(self):
    alias = None
    if self.alias:
        alias = self.alias
    elif self.auto_alias:
        alias = self.auto_alias
    return alias