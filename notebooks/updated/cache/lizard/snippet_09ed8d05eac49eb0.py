def release(self, shortname):
    url = 'api/v6/releases/?shortname=%s' % shortname
    releases = yield self._get(url)
    if not releases:
        raise ReleaseNotFoundException('no release %s' % shortname)
    release = Release.fromDict(releases[0])
    release.connection = self
    defer.returnValue(release)