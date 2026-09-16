def sticky(self, bottom=True):
    url = self.reddit_session.config['sticky_submission']
    data = {'id': self.fullname, 'state': True}
    if not bottom:
        data['num'] = 1
    return self.reddit_session.request_json(url, data=data)