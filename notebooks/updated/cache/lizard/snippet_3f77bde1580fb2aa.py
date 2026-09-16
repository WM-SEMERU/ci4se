def _get(self, path):
    url = self._get_url(path)
    try:
        response = urllib2.urlopen(url)
    except Exception as err:
        self.log.error('%s: %s', url, err)
        return False
    try:
        doc = json.load(response)
    except (TypeError, ValueError):
        self.log.error('Unable to parse response from Mesos as a json object')
        return False
    return doc