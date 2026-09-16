def set_position_target_global_int_send(self, time_boot_ms, target_system,
    target_component, coordinate_frame, type_mask, lat_int, lon_int, alt,
    vx, vy, vz, afx, afy, afz, yaw, yaw_rate, force_mavlink1=False):
    return self.send(self.set_position_target_global_int_encode(
        time_boot_ms, target_system, target_component, coordinate_frame,
        type_mask, lat_int, lon_int, alt, vx, vy, vz, afx, afy, afz, yaw,
        yaw_rate), force_mavlink1=force_mavlink1)