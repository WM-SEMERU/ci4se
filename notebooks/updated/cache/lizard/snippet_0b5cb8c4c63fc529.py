def scaled_imu3_send(self, time_boot_ms, xacc, yacc, zacc, xgyro, ygyro,
    zgyro, xmag, ymag, zmag, force_mavlink1=False):
    return self.send(self.scaled_imu3_encode(time_boot_ms, xacc, yacc, zacc,
        xgyro, ygyro, zgyro, xmag, ymag, zmag), force_mavlink1=force_mavlink1)