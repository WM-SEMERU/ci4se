def owned_by(self, owner, also_check_group=False):
    if also_check_group:
        return self.owner == owner and self.group == owner
    else:
        return self.owner == owner