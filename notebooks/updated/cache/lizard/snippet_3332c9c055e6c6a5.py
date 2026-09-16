def userstream_user(self, delegate, stall_warnings=None, with_='followings',
    replies=None):
    params = {'stringify_friend_ids': 'true'}
    set_bool_param(params, 'stall_warnings', stall_warnings)
    set_str_param(params, 'with', with_)
    set_str_param(params, 'replies', replies)
    svc = TwitterStreamService(lambda : self._get_userstream('user.json',
        params), delegate)
    return svc