def _zd_decode(self, msg):
    zone_definitions = [(ord(x) - 48) for x in msg[4:4 + Max.ZONES.value]]
    return {'zone_definitions': zone_definitions}