def vote(self, direction=0):
    url = self.reddit_session.config['vote']
    data = {'id': self.fullname, 'dir': six.text_type(direction)}
    if self.reddit_session.user:
        urls = [urljoin(self.reddit_session.user._url, 'disliked'), urljoin
            (self.reddit_session.user._url, 'liked')]
        self.reddit_session.evict(urls)
    return self.reddit_session.request_json(url, data=data)