def get_upvoted(self, *args, **kwargs):
    kwargs['_use_oauth'] = self.reddit_session.is_oauth_session()
    return _get_redditor_listing('upvoted')(self, *args, **kwargs)