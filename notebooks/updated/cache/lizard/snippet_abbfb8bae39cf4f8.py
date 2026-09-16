def resources(self, absolute_url=None):
    if absolute_url:
        return Resources(mode='server', root_url=absolute_url + self.
            _prefix, path_versioner=StaticHandler.append_version)
    return Resources(mode='server', root_url=self._prefix, path_versioner=
        StaticHandler.append_version)