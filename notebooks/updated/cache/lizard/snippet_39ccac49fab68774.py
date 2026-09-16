def statuses_retweets(self, id, count=None, trim_user=None):
    params = {'id': id}
    set_int_param(params, 'count', count)
    set_bool_param(params, 'trim_user', trim_user)
    return self._get_api('statuses/retweets.json', params)