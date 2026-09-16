def set_color(self, red, green, blue):
    if self._pwm_enabled:
        rdc, gdc, bdc = self._rgb_to_duty_cycle((red, green, blue))
        self._red.pwm_start(rdc)
        self._green.pwm.start(gdc)
        self._blue.pwm.start(bdc)
    else:
        self._red.set(self._blpol if red else not self._blpol)
        self._green.set(self._blpol if green else not self._blpol)
        self._blue.set(self._blpol if blue else not self._blpol)