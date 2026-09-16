def init(self):
    self.credentials = self._get_credentials()
    self.http = self.credentials.authorize(httplib2.Http())
    self.service = discovery.build('sheets', 'v4', http=self.http,
        discoveryServiceUrl=DISCOVERY_URL)