def received_new(self, msg):
    logger.info('Receiving msg, delivering to Lamson...')
    logger.debug('Relaying msg to lamson: From: %s, To: %s', msg['From'],
        msg['To'])
    self._relay.deliver(msg)