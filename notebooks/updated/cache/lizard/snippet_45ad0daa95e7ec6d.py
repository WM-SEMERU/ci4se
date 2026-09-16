def update(self):
    if not self._ok:
        self.log_error('Trying to restore OK mode w/ soft reset')
        self._ok = self._soft_reset()
    try:
        self._bus.write_byte(self._i2c_add, CMD_READ_TEMP_NOHOLD)
        sleep(MEASUREMENT_WAIT_TIME)
        buf_t = self._bus.read_i2c_block_data(self._i2c_add,
            CMD_READ_TEMP_HOLD, 3)
        self._bus.write_byte(self._i2c_add, CMD_READ_HUM_NOHOLD)
        sleep(MEASUREMENT_WAIT_TIME)
        buf_h = self._bus.read_i2c_block_data(self._i2c_add,
            CMD_READ_HUM_HOLD, 3)
    except OSError as exc:
        self._ok = False
        self.log_error('Bad reading: %s', exc)
        return
    if self._crc8check(buf_t):
        temp = (buf_t[0] << 8 | buf_t[1]) & 65532
        self._temperature = self._calc_temp(temp)
        if self._crc8check(buf_h):
            humid = (buf_h[0] << 8 | buf_h[1]) & 65532
            rh_actual = self._calc_humid(humid)
            rh_final = self._temp_coefficient(rh_actual, self._temperature)
            rh_final = 100.0 if rh_final > 100 else rh_final
            rh_final = 0.0 if rh_final < 0 else rh_final
            self._humidity = rh_final
        else:
            self._humidity = -255
            self._ok = False
            self.log_error('Bad CRC error with humidity')
    else:
        self._temperature = -255
        self._ok = False
        self.log_error('Bad CRC error with temperature')