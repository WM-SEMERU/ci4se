def get_archive_url(self):
    headers, data = self._requester.requestJsonAndCheck('GET', self.url +
        '/archive', headers={'Accept': Consts.mediaTypeMigrationPreview})
    return data['data']