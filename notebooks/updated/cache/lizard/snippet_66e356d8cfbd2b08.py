def redirect_to(self, url=None, parameters={}):
    if url is None and 'RelayState' in self.__request_data['get_data']:
        url = self.__request_data['get_data']['RelayState']
    return OneLogin_Saml2_Utils.redirect(url, parameters, request_data=self
        .__request_data)