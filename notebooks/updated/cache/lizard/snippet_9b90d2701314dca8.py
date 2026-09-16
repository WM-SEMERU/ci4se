def callback_oauth2(self, request):
    callback_url = self.callback_url(request)
    oauth = OAuth2Session(client_id=self.consumer_key, redirect_uri=
        callback_url, scope=self.scope)
    request_token = oauth.fetch_token(self.REQ_TOKEN, code=request.GET.get(
        'code', ''), authorization_response=callback_url, client_secret=
        self.consumer_secret, scope=self.scope, verify=False)
    return request_token.get('access_token')