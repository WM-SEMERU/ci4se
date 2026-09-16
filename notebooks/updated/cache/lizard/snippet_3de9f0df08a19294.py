def user_timeline(self, delegate, user=None, params={}, extra_args=None):
    if user:
        params['id'] = user
    return self.__get('/statuses/user_timeline.xml', delegate, params, txml
        .Statuses, extra_args=extra_args)