def retract(self, safety_margin=10):
    self.previous_placeable = None
    self.robot.poses = self.instrument_mover.fast_home(self.robot.poses,
        safety_margin)
    return self