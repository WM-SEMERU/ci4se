def ahrs2_encode(self, roll, pitch, yaw, altitude, lat, lng):
    return MAVLink_ahrs2_message(roll, pitch, yaw, altitude, lat, lng)