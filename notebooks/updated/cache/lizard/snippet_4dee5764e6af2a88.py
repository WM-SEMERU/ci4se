def airspeeds_encode(self, time_boot_ms, airspeed_imu, airspeed_pitot,
    airspeed_hot_wire, airspeed_ultrasonic, aoa, aoy):
    return MAVLink_airspeeds_message(time_boot_ms, airspeed_imu,
        airspeed_pitot, airspeed_hot_wire, airspeed_ultrasonic, aoa, aoy)