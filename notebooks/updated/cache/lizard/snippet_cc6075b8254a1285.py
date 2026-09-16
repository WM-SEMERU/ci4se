def dynamic_filter(self):
    url = ('https://stream.twitter.com/%s/statuses/filter.json' % self.
        streamer.api_version)
    self.streamer._request(url, 'POST', params=self.params)