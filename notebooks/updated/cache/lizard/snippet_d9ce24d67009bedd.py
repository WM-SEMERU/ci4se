def get(self, uri, params={}):
    logging.debug('Requesting URL: ' + str(urlparse.urljoin(self.BASE_URL,
        uri)))
    return requests.get(urlparse.urljoin(self.BASE_URL, uri), params=params,
        verify=False, auth=self.auth)