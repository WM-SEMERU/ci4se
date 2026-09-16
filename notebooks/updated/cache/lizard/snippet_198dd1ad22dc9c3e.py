def get_raw_data(self):
    r = self._readU16LE(TCS34725_RDATAL)
    g = self._readU16LE(TCS34725_GDATAL)
    b = self._readU16LE(TCS34725_BDATAL)
    c = self._readU16LE(TCS34725_CDATAL)
    time.sleep(INTEGRATION_TIME_DELAY[self._integration_time])
    return r, g, b, c