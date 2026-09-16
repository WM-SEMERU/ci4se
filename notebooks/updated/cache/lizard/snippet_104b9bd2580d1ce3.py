def cpu_speed(self, silent=False):
    res = self._dll.JLINKARM_MeasureCPUSpeedEx(-1, 1, int(silent))
    if res < 0:
        raise errors.JLinkException(res)
    return res