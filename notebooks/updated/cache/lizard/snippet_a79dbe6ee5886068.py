def read_proximity(self, timeout_sec=1):
    self._device.write8(VCNL40xx_COMMAND, VCNL40xx_MEASUREPROXIMITY)
    self._wait_response(VCNL40xx_PROXIMITYREADY, timeout_sec)
    return self._device.readU16BE(VCNL40xx_PROXIMITYDATA)