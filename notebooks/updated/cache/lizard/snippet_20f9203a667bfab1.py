def set_actuator_control_target_send(self, time_usec, group_mlx,
    target_system, target_component, controls, force_mavlink1=False):
    return self.send(self.set_actuator_control_target_encode(time_usec,
        group_mlx, target_system, target_component, controls),
        force_mavlink1=force_mavlink1)