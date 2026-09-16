def update(self, gist, content):
    if content is False:
        return False
    url = self._api_url('gists', gist.get('id'))
    data = {'files': {self.filename: {'content': content}}}
    self.output('Sending contents of {} to {}'.format(self.file_path, url))
    response = self.requests.patch(url, data=dumps(data))
    if response.status_code != 200:
        self.oops('Could not update ' + gist.get('description'))
        self.oops('PATCH request returned ' + str(response.status_code))
        return False
    self.yeah('Done!')
    self.hey('The URL to this Gist is: {}'.format(gist['url']))
    return True