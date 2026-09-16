def create_version(self, name, project, description=None, releaseDate=None,
    startDate=None, archived=False, released=False):
    data = {'name': name, 'project': project, 'archived': archived,
        'released': released}
    if description is not None:
        data['description'] = description
    if releaseDate is not None:
        data['releaseDate'] = releaseDate
    if startDate is not None:
        data['startDate'] = startDate
    url = self._get_url('version')
    r = self._session.post(url, data=json.dumps(data))
    time.sleep(1)
    version = Version(self._options, self._session, raw=json_loads(r))
    return version