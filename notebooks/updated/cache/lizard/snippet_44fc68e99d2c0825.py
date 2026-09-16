def set_flow_rate(self, aspirate=None, dispense=None):
    ul = self.max_volume
    if aspirate:
        ul_per_mm = self._ul_per_mm(ul, 'aspirate')
        self.set_speed(aspirate=round(aspirate / ul_per_mm, 6))
    if dispense:
        ul_per_mm = self._ul_per_mm(ul, 'dispense')
        self.set_speed(dispense=round(dispense / ul_per_mm, 6))
    return self