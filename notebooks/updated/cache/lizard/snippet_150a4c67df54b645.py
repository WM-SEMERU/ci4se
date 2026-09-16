def open(self):
    self.clearException()
    try:
        if self._isOpen:
            logger.warn(
                'Resources already open. Closing them first before opening.')
            self._closeResources()
            self._isOpen = False
        assert not self._isOpen, 'Sanity check failed: _isOpen should be false'
        logger.debug('Opening {}'.format(self))
        self._openResources()
        self._isOpen = True
        if self.model:
            self.model.sigItemChanged.emit(self)
        else:
            logger.warning('Model not set yet: {}'.format(self))
    except Exception as ex:
        if DEBUGGING:
            raise
        logger.exception('Error during tree item open: {}'.format(ex))
        self.setException(ex)