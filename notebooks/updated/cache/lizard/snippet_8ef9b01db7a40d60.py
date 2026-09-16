def dispense(self, volume=None, location=None, rate=1.0):
    if not self.tip_attached:
        log.warning('Cannot dispense without a tip attached.')
    if not helpers.is_number(volume):
        if volume and not location:
            location = volume
        volume = self.current_volume
    volume = min(self.current_volume, volume)
    display_location = location if location else self.previous_placeable
    do_publish(self.broker, commands.dispense, self.dispense, 'before',
        None, None, self, volume, display_location, rate)
    if volume != 0:
        self._position_for_dispense(location)
        mm_position = self._dispense_plunger_position(self.current_volume -
            volume)
        speed = self.speeds['dispense'] * rate
        self.instrument_actuator.push_speed()
        self.instrument_actuator.set_speed(speed)
        self.instrument_actuator.set_active_current(self._plunger_current)
        self.robot.poses = self.instrument_actuator.move(self.robot.poses,
            x=mm_position)
        self.instrument_actuator.pop_speed()
        self.current_volume -= volume
    do_publish(self.broker, commands.dispense, self.dispense, 'after', self,
        None, self, volume, display_location, rate)
    return self