def logout(self):
    logger.debug('Logout')
    method = self._anaconda_client_api.remove_authentication
    return self._create_worker(method)