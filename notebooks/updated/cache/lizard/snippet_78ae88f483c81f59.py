def optical_flow_rad_send(self, time_usec, sensor_id, integration_time_us,
    integrated_x, integrated_y, integrated_xgyro, integrated_ygyro,
    integrated_zgyro, temperature, quality, time_delta_distance_us,
    distance, force_mavlink1=False):
    return self.send(self.optical_flow_rad_encode(time_usec, sensor_id,
        integration_time_us, integrated_x, integrated_y, integrated_xgyro,
        integrated_ygyro, integrated_zgyro, temperature, quality,
        time_delta_distance_us, distance), force_mavlink1=force_mavlink1)