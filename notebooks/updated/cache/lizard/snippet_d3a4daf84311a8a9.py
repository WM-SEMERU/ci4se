def can_view(self, user):
    return user in self.group.users or self.project.can_view(user)