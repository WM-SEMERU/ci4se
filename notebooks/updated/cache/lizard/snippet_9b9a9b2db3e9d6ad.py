def manual_setpoint_send(self, time_boot_ms, roll, pitch, yaw, thrust,
    mode_switch, manual_override_switch, force_mavlink1=False):
    return self.send(self.manual_setpoint_encode(time_boot_ms, roll, pitch,
        yaw, thrust, mode_switch, manual_override_switch), force_mavlink1=
        force_mavlink1)