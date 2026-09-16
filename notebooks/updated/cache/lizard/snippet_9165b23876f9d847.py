def update_subnet(self, subnet, body=None):
    return self.put(self.subnet_path % subnet, body=body)