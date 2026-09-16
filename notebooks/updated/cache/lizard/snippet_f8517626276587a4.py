def get_public_ip(self, addr_family=None, *args, **kwargs):
    return self.get_ip('public', addr_family, *args, **kwargs)