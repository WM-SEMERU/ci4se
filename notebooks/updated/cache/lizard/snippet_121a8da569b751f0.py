def venue_stocks(self):
    url = urljoin(self.base_url, 'venues/{0}/stocks'.format(self.venue))
    return self.session.get(url).json()