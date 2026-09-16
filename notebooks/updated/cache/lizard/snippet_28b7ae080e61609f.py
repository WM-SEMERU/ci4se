def available_settings(self):
    available = {}
    if not self.status_data:
        return available
    for key, val in self.status_data.get('avail', {}).items():
        available[key] = []
        for subval in val:
            try:
                subval = float(subval)
            except ValueError:
                subval = subval
            if val in ('on', 'off'):
                subval = subval == 'on'
            available[key].append(subval)
    return available