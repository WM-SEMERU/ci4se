def srem(self, key, member, *members):
    return self.execute(b'SREM', key, member, *members)