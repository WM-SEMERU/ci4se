def addProxyObject(self, obj, proxied):
    self.proxied_objects[id(obj)] = proxied
    self.proxied_objects[id(proxied)] = obj