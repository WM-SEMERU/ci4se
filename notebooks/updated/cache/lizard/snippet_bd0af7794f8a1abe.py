def default_subreddits(self, *args, **kwargs):
    url = self.config['default_subreddits']
    return self.get_content(url, *args, **kwargs)