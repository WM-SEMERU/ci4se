def _assign_zones(self):
    for zone_id in range(1, 5):
        zone = RainCloudyFaucetZone(parent=self._parent, controller=self.
            _controller, faucet=self, zone_id=zone_id)
        if zone not in self.zones:
            self.zones.append(zone)