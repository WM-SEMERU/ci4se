def containers(self):
    return [self.client.containers.get(cid) for cid in (self.attrs.get(
        'Containers') or {}).keys()]