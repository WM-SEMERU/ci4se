def hil_state_quaternion_encode(self, time_usec, attitude_quaternion,
    rollspeed, pitchspeed, yawspeed, lat, lon, alt, vx, vy, vz,
    ind_airspeed, true_airspeed, xacc, yacc, zacc):
    return MAVLink_hil_state_quaternion_message(time_usec,
        attitude_quaternion, rollspeed, pitchspeed, yawspeed, lat, lon, alt,
        vx, vy, vz, ind_airspeed, true_airspeed, xacc, yacc, zacc)