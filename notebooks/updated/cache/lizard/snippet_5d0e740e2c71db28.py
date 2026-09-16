def get(self, *args, **kwargs):
    payload = self.buf.get(*args, **kwargs)
    logger.debug('Removing RPC payload from ControlBuffer queue: %s', payload)
    return payload