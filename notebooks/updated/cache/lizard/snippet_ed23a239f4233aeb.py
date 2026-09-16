def manual_control_send(self, target, x, y, z, r, buttons, force_mavlink1=False
    ):
    return self.send(self.manual_control_encode(target, x, y, z, r, buttons
        ), force_mavlink1=force_mavlink1)