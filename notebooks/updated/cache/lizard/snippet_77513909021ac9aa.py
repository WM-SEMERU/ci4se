def to_json(self):
    json_dict = self.to_json_basic()
    json_dict['pulses'] = self.pulses
    json_dict['counter'] = self.counter
    json_dict['kwh'] = self.kwh
    json_dict['delay'] = self.delay
    json_dict['watt'] = self.watt
    json_dict['channel'] = self.channel
    return json.dumps(json_dict)