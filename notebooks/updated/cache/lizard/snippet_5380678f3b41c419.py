def gild(self, months=None):
    if isinstance(self, Redditor):
        months = int(months) if months is not None else 1
        if months < 1:
            raise TypeError('months must be at least 1')
        if months > 36:
            raise TypeError('months must be no more than 36')
        response = self.reddit_session.request(self.reddit_session.config[
            'gild_user'].format(username=six.text_type(self)), data={
            'months': months})
    elif months is not None:
        raise TypeError('months is not a valid parameter for {0}'.format(
            type(self)))
    else:
        response = self.reddit_session.request(self.reddit_session.config[
            'gild_thing'].format(fullname=self.fullname), data=True)
    return response.status_code == 200