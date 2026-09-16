def swo_enable(self, cpu_speed, swo_speed=9600, port_mask=1):
    if self.swo_enabled():
        self.swo_stop()
    res = self._dll.JLINKARM_SWO_EnableTarget(cpu_speed, swo_speed, enums.
        JLinkSWOInterfaces.UART, port_mask)
    if res != 0:
        raise errors.JLinkException(res)
    self._swo_enabled = True
    return None