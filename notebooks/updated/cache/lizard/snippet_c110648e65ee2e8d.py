def assign(self, role):
    if role.owner_id != self.id:
        return self.roles.add(role)