def refresh_data(self):
    j = self.data_request({'id': 'sdata'}).json()
    self.temperature_units = j.get('temperature', 'C')
    self.model = j.get('model')
    self.version = j.get('version')
    self.serial_number = j.get('serial_number')
    categories = {}
    cats = j.get('categories')
    for cat in cats:
        categories[cat.get('id')] = cat.get('name')
    device_id_map = {}
    devs = j.get('devices')
    for dev in devs:
        dev['categoryName'] = categories.get(dev.get('category'))
        device_id_map[dev.get('id')] = dev
    return device_id_map