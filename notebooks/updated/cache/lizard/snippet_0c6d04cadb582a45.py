def on_for_rotations(self, left_speed, right_speed, rotations, brake=True,
    block=True):
    MoveTank.on_for_degrees(self, left_speed, right_speed, rotations * 360,
        brake, block)