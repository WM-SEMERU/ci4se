def altitude_send(self, time_usec, altitude_monotonic, altitude_amsl,
    altitude_local, altitude_relative, altitude_terrain, bottom_clearance,
    force_mavlink1=False):
    return self.send(self.altitude_encode(time_usec, altitude_monotonic,
        altitude_amsl, altitude_local, altitude_relative, altitude_terrain,
        bottom_clearance), force_mavlink1=force_mavlink1)