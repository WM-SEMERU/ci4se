def attributes(self):
    attributes = {'name': self.name, 'camera_id': self.camera_id, 'serial':
        self.serial, 'temperature': self.temperature, 'temperature_c': self
        .temperature_c, 'temperature_calibrated': self.
        temperature_calibrated, 'battery': self.battery, 'thumbnail': self.
        thumbnail, 'video': self.clip, 'motion_enabled': self.
        motion_enabled, 'motion_detected': self.motion_detected,
        'wifi_strength': self.wifi_strength, 'network_id': self.sync.
        network_id, 'sync_module': self.sync.name, 'last_record': self.
        last_record}
    return attributes