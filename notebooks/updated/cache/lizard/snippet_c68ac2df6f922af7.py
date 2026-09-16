def all_units_idle(self):
    for unit in self.units.values():
        unit_status = unit.data['agent-status']['current']
        if unit_status != 'idle':
            return False
    return True