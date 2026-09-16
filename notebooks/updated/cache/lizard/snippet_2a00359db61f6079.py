def global_position_int_send(self, time_boot_ms, lat, lon, alt,
    relative_alt, vx, vy, vz, hdg, force_mavlink1=False):
    return self.send(self.global_position_int_encode(time_boot_ms, lat, lon,
        alt, relative_alt, vx, vy, vz, hdg), force_mavlink1=force_mavlink1)