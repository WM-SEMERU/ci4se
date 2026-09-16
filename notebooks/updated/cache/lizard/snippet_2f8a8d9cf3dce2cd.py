def get_member(self, name):
    for member in self.members:
        if member.name == name:
            return member
    return None