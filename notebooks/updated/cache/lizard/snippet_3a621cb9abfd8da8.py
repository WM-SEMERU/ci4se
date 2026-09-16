def user_data(self, access_token, *args, **kwargs):
    url = GOOGLE_APPENGINE_PROFILE_V1
    auth = self.oauth_auth(access_token)
    return self.get_json(url, auth=auth, params=auth)