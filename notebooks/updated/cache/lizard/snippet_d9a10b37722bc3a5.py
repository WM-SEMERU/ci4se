def coresight_write(self, reg, data, ap=True):
    ap = 1 if ap else 0
    res = self._dll.JLINKARM_CORESIGHT_WriteAPDPReg(reg, ap, data)
    if res < 0:
        raise errors.JLinkException(res)
    return res