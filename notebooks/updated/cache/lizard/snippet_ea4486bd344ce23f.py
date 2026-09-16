def is_acquired(self):
    uuid, _ = self.etcd_client.get(self.key)
    if uuid is None:
        return False
    return uuid == self.uuid