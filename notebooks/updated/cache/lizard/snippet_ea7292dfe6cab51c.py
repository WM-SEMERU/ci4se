def create_api_environment(self):
    return ApiEnvironment(self.networkapi_url, self.user, self.password,
        self.user_ldap)