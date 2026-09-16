def networks(self):
    import ns1.rest.ipam
    return ns1.rest.ipam.Networks(self.config)