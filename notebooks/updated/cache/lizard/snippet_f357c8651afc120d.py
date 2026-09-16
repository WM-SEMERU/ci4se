def remove(self, member):
    if not self.client.zrem(self.name, member):
        raise KeyError(member)