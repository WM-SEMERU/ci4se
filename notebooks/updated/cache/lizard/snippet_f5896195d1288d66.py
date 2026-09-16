def message_interval_send(self, message_id, interval_us, force_mavlink1=False):
    return self.send(self.message_interval_encode(message_id, interval_us),
        force_mavlink1=force_mavlink1)