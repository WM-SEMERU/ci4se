def update_flavor(self, flavor, body):
    return self.put(self.flavor_path % flavor, body=body)