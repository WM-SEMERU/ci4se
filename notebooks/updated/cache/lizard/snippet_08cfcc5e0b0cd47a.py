def remove_release(self, username, package_name, version):
    url = '%s/release/%s/%s/%s' % (self.domain, username, package_name, version
        )
    res = self.session.delete(url)
    self._check_response(res, [201])
    return