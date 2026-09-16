def connect(self, forceReconnect=False):
    if self._state == 'stopped':
        raise Error('This service is not running. Not connecting.')
    if self._state == 'connected':
        if forceReconnect:
            self._toState('disconnecting')
            return True
        else:
            raise ConnectError('Already connected.')
    elif self._state == 'aborting':
        raise ConnectError('Aborting connection in progress.')
    elif self._state == 'disconnecting':
        raise ConnectError('Disconnect in progress.')
    elif self._state == 'connecting':
        if forceReconnect:
            self._toState('aborting')
            return True
        else:
            raise ConnectError('Connect in progress.')
    if self.delegate is None:
        if self._state != 'idle':
            self._toState('idle')
        raise NoConsumerError()
    if self._state == 'waiting':
        if self._reconnectDelayedCall.called:
            self._reconnectDelayedCall = None
            pass
        else:
            self._reconnectDelayedCall.reset(0)
            return True
    self._toState('connecting')
    return True