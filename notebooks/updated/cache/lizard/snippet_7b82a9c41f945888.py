def mount_status_send(self, target_system, target_component, pointing_a,
    pointing_b, pointing_c, force_mavlink1=False):
    return self.send(self.mount_status_encode(target_system,
        target_component, pointing_a, pointing_b, pointing_c),
        force_mavlink1=force_mavlink1)