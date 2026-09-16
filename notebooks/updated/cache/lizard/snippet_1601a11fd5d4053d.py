def get(self, name, failobj=None):
    name = name.lower()
    for k, v in self._headers:
        if k.lower() == name:
            return self.policy.header_fetch_parse(k, v)
    return failobj