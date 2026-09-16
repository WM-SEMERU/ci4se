def post(self, url, post_params=None):
    params = urlencode(post_params)
    logger.debug('Making POST request to %s with body %s', url, params)
    return self.oauth_session.post(url, data=params)