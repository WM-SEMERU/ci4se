def getProvince(self, default=None):
    physical_address = self.getPhysicalAddress().get('state', default)
    postal_address = self.getPostalAddress().get('state', default)
    return physical_address or postal_address