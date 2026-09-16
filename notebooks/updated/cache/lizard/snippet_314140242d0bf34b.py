def control_system_state_send(self, time_usec, x_acc, y_acc, z_acc, x_vel,
    y_vel, z_vel, x_pos, y_pos, z_pos, airspeed, vel_variance, pos_variance,
    q, roll_rate, pitch_rate, yaw_rate, force_mavlink1=False):
    return self.send(self.control_system_state_encode(time_usec, x_acc,
        y_acc, z_acc, x_vel, y_vel, z_vel, x_pos, y_pos, z_pos, airspeed,
        vel_variance, pos_variance, q, roll_rate, pitch_rate, yaw_rate),
        force_mavlink1=force_mavlink1)