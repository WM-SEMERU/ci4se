def flexifunction_directory_ack_send(self, target_system, target_component,
    directory_type, start_index, count, result, force_mavlink1=False):
    return self.send(self.flexifunction_directory_ack_encode(target_system,
        target_component, directory_type, start_index, count, result),
        force_mavlink1=force_mavlink1)