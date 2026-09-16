def get(self, key, get_cas=False):
    for server in self.servers:
        value, cas = server.get(key)
        if value is not None:
            if get_cas:
                return value, cas
            else:
                return value
    if get_cas:
        return None, None