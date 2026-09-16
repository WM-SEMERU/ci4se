def setTxPower(self, tx_power):
    tx_pow_validated = self.get_tx_power(tx_power)
    logger.debug('tx_pow_validated: %s', tx_pow_validated)
    needs_update = False
    for ant, (tx_pow_idx, tx_pow_dbm) in tx_pow_validated.items():
        if self.tx_power[ant] != tx_pow_idx:
            self.tx_power[ant] = tx_pow_idx
            needs_update = True
        logger.debug('tx_power for antenna %s: %s (%s dBm)', ant,
            tx_pow_idx, tx_pow_dbm)
    if needs_update and self.state == LLRPClient.STATE_INVENTORYING:
        logger.debug('changing tx power; will stop politely, then resume')
        d = self.stopPolitely()
        d.addCallback(self.startInventory, force_regen_rospec=True)