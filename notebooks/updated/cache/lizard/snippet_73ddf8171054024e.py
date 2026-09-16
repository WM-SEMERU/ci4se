def artUrl(self):
    art = self.firstAttr('art', 'grandparentArt')
    return self._server.url(art, includeToken=True) if art else None