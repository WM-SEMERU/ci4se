def get_banned(self, subreddit, user_only=True, *args, **kwargs):
    url = self.config['banned'].format(subreddit=six.text_type(subreddit))
    return self._get_userlist(url, user_only, *args, **kwargs)