def attitude_target_send(self, time_boot_ms, type_mask, q, body_roll_rate,
    body_pitch_rate, body_yaw_rate, thrust, force_mavlink1=False):
    return self.send(self.attitude_target_encode(time_boot_ms, type_mask, q,
        body_roll_rate, body_pitch_rate, body_yaw_rate, thrust),
        force_mavlink1=force_mavlink1)