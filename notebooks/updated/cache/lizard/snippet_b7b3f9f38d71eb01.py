def filename(self):
    if self.value and 'value' in self._json_data and self._json_data['value']:
        return self._json_data['value'].split('/')[-1]
    return None