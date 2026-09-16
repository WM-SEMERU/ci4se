def _set_container(self, container):
    if self.use_pyrax:
        if container.cdn_ttl != self.ttl or not container.cdn_enabled:
            container.make_public(ttl=self.ttl)
        if hasattr(self, '_container_public_uri'):
            delattr(self, '_container_public_uri')
    self._container = container