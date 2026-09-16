def read_adc(self, adc_number):
    assert 0 <= adc_number <= 7, 'ADC number must be a value of 0-7!'
    command = 3 << 6
    command |= (adc_number & 7) << 3
    resp = self._spi.transfer([command, 0, 0])
    result = (resp[0] & 1) << 9
    result |= (resp[1] & 255) << 1
    result |= (resp[2] & 128) >> 7
    return result & 1023