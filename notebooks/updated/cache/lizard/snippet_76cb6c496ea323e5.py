def read_segment(self, segment):
    log.debug('read segment {0}'.format(segment))
    if segment < 0 or segment > 15:
        raise ValueError('invalid segment number')
    cmd = '\x10' + chr(segment << 4) + 8 * chr(0) + self.uid
    rsp = self.transceive(cmd)
    if len(rsp) < 129:
        raise Type1TagCommandError(RESPONSE_ERROR)
    return rsp[1:129]