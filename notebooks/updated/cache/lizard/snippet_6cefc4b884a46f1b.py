def _container_whitelist(self):
    if self.__container_whitelist is None:
        self.__container_whitelist = set(self.
            CLOUD_BROWSER_CONTAINER_WHITELIST or [])
    return self.__container_whitelist