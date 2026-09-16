def _position_for_aspirate(self, location=None, clearance=1.0):
    placeable = None
    if location:
        placeable, _ = unpack_location(location)
        if placeable != self.previous_placeable:
            self.move_to(placeable.top())
    else:
        placeable = self.previous_placeable
    if self.current_volume == 0:
        pos, _, _ = pose_tracker.absolute(self.robot.poses, self.
            instrument_actuator)
        if pos != self._get_plunger_position('bottom'):
            if placeable:
                self.move_to(placeable.top())
            self.instrument_actuator.set_active_current(self._plunger_current)
            self.robot.poses = self.instrument_actuator.move(self.robot.
                poses, x=self._get_plunger_position('bottom'))
    if location:
        if isinstance(location, Placeable):
            location = location.bottom(min(location.z_size(), clearance))
        self.move_to(location, strategy='direct')