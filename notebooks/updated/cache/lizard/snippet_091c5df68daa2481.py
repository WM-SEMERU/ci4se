def Delete(self):
    self.public_ip.source_restrictions = [o for o in self.public_ip.
        source_restrictions if o != self]
    return self.public_ip.Update()