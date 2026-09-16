def set_prekeys_as_sent(self, prekeyIds):
    logger.debug('set_prekeys_as_sent(prekeyIds=[%d prekeyIds])' % len(
        prekeyIds))
    self._store.preKeyStore.setAsSent([prekey.getId() for prekey in prekeyIds])