def provider_id_slot(self, other):
    if other:
        pid = other.provider_id()
        for i, provider in enumerate(self.providers):
            if provider.provider_id() == pid:
                return i
    return None