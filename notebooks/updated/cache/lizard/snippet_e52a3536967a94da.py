def sendDtmfTone(self, tones):
    if self.answered:
        dtmfCommandBase = self.DTMF_COMMAND_BASE.format(cid=self.id)
        toneLen = len(tones)
        if len(tones) > 1:
            cmd = ('AT{0}{1};{0}' + ';{0}'.join(tones[1:])).format(
                dtmfCommandBase, tones[0])
        else:
            cmd = 'AT{0}{1}'.format(dtmfCommandBase, tones)
        try:
            self._gsmModem.write(cmd, timeout=5 + toneLen)
        except CmeError as e:
            if e.code == 30:
                raise InterruptedException('No network service', e)
            elif e.code == 3:
                raise InterruptedException('Operation not allowed', e)
            else:
                raise e
    else:
        raise InvalidStateException(
            'Call is not active (it has not yet been answered, or it has ended).'
            )