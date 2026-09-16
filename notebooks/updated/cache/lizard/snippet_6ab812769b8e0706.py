def terrain_report_send(self, lat, lon, spacing, terrain_height,
    current_height, pending, loaded, force_mavlink1=False):
    return self.send(self.terrain_report_encode(lat, lon, spacing,
        terrain_height, current_height, pending, loaded), force_mavlink1=
        force_mavlink1)