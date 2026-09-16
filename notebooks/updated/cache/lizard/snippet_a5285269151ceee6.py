def get_multireddits(self, redditor, *args, **kwargs):
    redditor = six.text_type(redditor)
    url = self.config['multireddit_user'].format(user=redditor)
    return self.request_json(url, *args, **kwargs)