def to_ip(self, values, from_unit):
    if from_unit in self._ip_units:
        return values, from_unit
    elif from_unit == 'degC-hours':
        return self.to_unit(values, 'degF-hours', from_unit), 'degF-hours'
    else:
        return self.to_unit(values, 'degF-days', from_unit), 'degF-days'