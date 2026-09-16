def post(self, url, postParameters=None, urlParameters=None):
    if not self.access_token:
        raise IOError('No authorized client available.')
    if not self.action_token:
        raise IOError('Need to generate action token.')
    if urlParameters is None:
        urlParameters = {}
    headers = {'Authorization': 'Bearer ' + self.access_token,
        'Content-Type': 'application/x-www-form-urlencoded'}
    postParameters.update({'T': self.action_token})
    request = requests.post(url + '?' + self.getParameters(urlParameters),
        data=postParameters, headers=headers)
    if request.status_code != 200:
        return None
    else:
        return toUnicode(request.text)