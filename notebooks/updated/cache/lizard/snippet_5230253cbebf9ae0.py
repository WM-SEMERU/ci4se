def nav_filter_bias_send(self, usec, accel_0, accel_1, accel_2, gyro_0,
    gyro_1, gyro_2, force_mavlink1=False):
    return self.send(self.nav_filter_bias_encode(usec, accel_0, accel_1,
        accel_2, gyro_0, gyro_1, gyro_2), force_mavlink1=force_mavlink1)