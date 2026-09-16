def OauthAuthorizeApplication(self, oauth_duration='hour'):
    if self.__session_id__ == '':
        self.__error__ = 'not logged in'
        return False
    parameters = {'oauth_token': self.__oauth_token__.key, 'tok_expir':
        self.__OauthGetTokExpir__(oauth_duration), 'action': 'ALLOW',
        'session_id': self.__session_id__}
    if self.__SenseApiCall__('/oauth/provider_authorize', 'POST',
        parameters=parameters):
        if self.__status__ == 302:
            response = urlparse.parse_qs(urlparse.urlparse(self.__headers__
                ['location'])[4])
            verifier = response['oauth_verifier'][0]
            self.__oauth_token__.set_verifier(verifier)
            return True
        else:
            self.__setAuthenticationMethod__('session_id')
            self.__error__ = 'error authorizing application'
            return False
    else:
        self.__setAuthenticationMethod__('session_id')
        self.__error__ = 'error authorizing application'
        return False