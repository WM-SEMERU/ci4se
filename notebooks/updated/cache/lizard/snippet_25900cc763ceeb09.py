def print_devices(self, devices):
    for device in devices:
        print('ID: {} OS: {} IP: {} State: {} ({}) Tags: {}'.format(device.
            id, device.operating_system.slug, self.get_public_ip(device.
            ip_addresses), device.state, 'spot' if device.spot_instance else
            'on-demand', device.tags))