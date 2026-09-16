def mission_count_send(self, target_system, target_component, count,
    force_mavlink1=False):
    return self.send(self.mission_count_encode(target_system,
        target_component, count), force_mavlink1=force_mavlink1)