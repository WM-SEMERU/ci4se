def _is_numeric_data(self, data_type):
    dt = DATA_TYPES[data_type]
    if dt['min'] and dt['max']:
        if type(self.data) is dt['type'] and dt['min'] < self.data < dt['max']:
            self.type = data_type.upper()
            self.len = len(str(self.data))
            return True