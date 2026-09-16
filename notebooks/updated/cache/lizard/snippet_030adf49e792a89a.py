def get_voltage(self, channel, unit='V'):
    kwargs = self._ch_map[channel]['ADCV']
    voltage_raw = self._get_adc_value(**kwargs)
    voltage = (voltage_raw - self._ch_cal[channel]['ADCV']['offset']
        ) / self._ch_cal[channel]['ADCV']['gain']
    if unit == 'raw':
        return voltage_raw
    elif unit == 'V':
        return voltage
    elif unit == 'mV':
        return voltage * 1000
    else:
        raise TypeError('Invalid unit type.')