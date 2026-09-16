def history(self):
    res = self._api_request('hist')
    if res[0][0] == '-1':
        raise PuushError('History retrieval failed.')
    files = []
    for line in res[1:]:
        id, upload_time, url, filename, views, _ = line
        files.append(self._File(id, url, filename, upload_time, views))
    return files