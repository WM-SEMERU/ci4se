def redirectURL(self, realm, return_to=None, immediate=False):
    message = self.getMessage(realm, return_to, immediate)
    return message.toURL(self.endpoint.server_url)