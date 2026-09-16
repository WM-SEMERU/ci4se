def get_driver(self, name, version):
    user_credentials = self.get_user_credentials()
    return discovery.build(name, version, http=self.authenticate(
        user_credentials))