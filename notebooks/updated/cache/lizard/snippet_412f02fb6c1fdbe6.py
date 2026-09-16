def add_priority(self, name, **attrs):
    return Priorities(self.requester).create(self.id, name, **attrs)