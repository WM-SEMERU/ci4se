def _parse_hwtype(self):
    self.chip_name = KNOWN_HARDWARE_TYPES.get(self.hw_type, 
        'Unknown Chip (type=%d)' % self.hw_type)