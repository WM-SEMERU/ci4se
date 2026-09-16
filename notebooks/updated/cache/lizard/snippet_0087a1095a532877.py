def destroy(self):
    r = self._h._http_resource(method='DELETE', resource=('apps', self.name))
    return r.ok