def adc_to_percentage(value, max_volts, clamp=True):
    percentage = 100.0 / const.ADC_MAX_VAL * value
    return max(min(100, percentage), 0) if clamp else percentage