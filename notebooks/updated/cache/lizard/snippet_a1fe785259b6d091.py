def login(self, password):
    self.bbox_auth.set_access(BboxConstant.AUTHENTICATION_LEVEL_PUBLIC,
        BboxConstant.AUTHENTICATION_LEVEL_PUBLIC)
    self.bbox_url.set_api_name('login', None)
    data = {'password': password}
    api = BboxApiCall(self.bbox_url, BboxConstant.HTTP_METHOD_POST, data,
        self.bbox_auth)
    response = api.execute_api_request()
    if response.status_code == 200:
        self.bbox_auth.set_cookie_id(response.cookies['BBOX_ID'])
    return self.bbox_auth.is_authentified()