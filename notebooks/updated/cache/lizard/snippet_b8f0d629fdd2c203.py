def _IsValidUrl(self, url):
    parsed_url = urlparse.urlparse(url)
    return parsed_url.scheme in self._SUPPORTED_URL_SCHEMES