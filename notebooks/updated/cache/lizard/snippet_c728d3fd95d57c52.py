def access(self, user):
    if self.denyusers:
        if user in self.denyusers:
            return False
    if self.allowusers:
        if not user in self.allowusers:
            return False
    return True