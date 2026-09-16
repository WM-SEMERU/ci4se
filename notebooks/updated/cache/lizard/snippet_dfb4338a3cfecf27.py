def get_user(self, user_name=None):
    params = {}
    if user_name:
        params['UserName'] = user_name
    return self.get_response('GetUser', params)