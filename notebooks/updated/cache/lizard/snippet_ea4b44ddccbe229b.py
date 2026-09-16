def start(self):
    if self._status == TransferState.PREPARING:
        super(Upload, self).start()
    else:
        raise SbgError('Unable to start. Upload not in PREPARING state.')