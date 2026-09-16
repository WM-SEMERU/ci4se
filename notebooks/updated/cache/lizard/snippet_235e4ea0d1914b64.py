def clear_cached_authorization_info(self, identifier):
    msg = 'Clearing cached authz_info for [{0}]'.format(identifier)
    logger.debug(msg)
    key = 'authorization:permissions:' + self.name
    self.cache_handler.delete(key, identifier)