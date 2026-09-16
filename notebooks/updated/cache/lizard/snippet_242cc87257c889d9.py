def get_location(self, ip, detailed=False):
    seek = self._get_pos(ip)
    if seek > 0:
        return self._parse_location(seek, detailed=detailed)
    return False