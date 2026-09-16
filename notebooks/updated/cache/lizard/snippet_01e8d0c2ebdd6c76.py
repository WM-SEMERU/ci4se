def initauth(self):
    headers = {'User-agent': 'CLAMClientAPI-' + clam.common.data.VERSION}
    if self.oauth:
        if not self.oauth_access_token:
            r = requests.get(self.url, headers=headers, verify=self.verify)
            if r.status_code == 404:
                raise clam.common.data.NotFound(
                    'Authorization provider not found')
            elif r.status_code == 403:
                raise clam.common.data.PermissionDenied(
                    'Authorization provider denies access')
            elif not (r.status_code >= 200 and r.status_code <= 299):
                raise Exception('An error occured, return code ' + str(r.
                    status_code))
            data = self._parse(r.text)
            if data is True:
                raise Exception(
                    'No access token provided, but Authorization Provider requires manual user input. Unable to authenticate automatically. Obtain an access token from '
                     + r.geturl())
            else:
                self.oauth_access_token = data.oauth_access_token
        headers['Authorization'] = 'Bearer ' + self.oauth_access_token
    return headers