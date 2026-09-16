def _update_state_from_response(self, response_json):
    power_strip = response_json.get('data')
    power_strip_reading = power_strip.get('last_reading')
    outlets = power_strip.get('outlets')
    for outlet in outlets:
        if outlet.get('outlet_id') == str(self.object_id()):
            outlet['last_reading']['connection'] = power_strip_reading.get(
                'connection')
            self.json_state = outlet