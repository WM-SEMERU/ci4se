def parse_region(self, login_response):
    auth_token = login_response.cgx_content['x_auth_token']
    auth_token_dict = self.parse_auth_token(auth_token)
    auth_region = auth_token_dict.get('region')
    return auth_region