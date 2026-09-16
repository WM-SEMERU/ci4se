def set_servo(self, gpio, pulse_width_us):
    _pulse_incr_us = _PWM.get_pulse_incr_us()
    if pulse_width_us % _pulse_incr_us:
        raise AttributeError(
            'Pulse width increment granularity %sus cannot divide a pulse-time of %sus'
             % (_pulse_incr_us, pulse_width_us))
    if _PWM.is_channel_initialized(self._dma_channel):
        _subcycle_us = _PWM.get_channel_subcycle_time_us(self._dma_channel)
        if _subcycle_us != self._subcycle_time_us:
            raise AttributeError(
                'Error: DMA channel %s is setup with a subcycle_time of %sus (instead of %sus)'
                 % (self._dma_channel, _subcycle_us, self._subcycle_time_us))
    else:
        init_channel(self._dma_channel, self._subcycle_time_us)
    add_channel_pulse(self._dma_channel, gpio, 0, int(pulse_width_us /
        _pulse_incr_us))