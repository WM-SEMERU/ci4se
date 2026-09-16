def parse(self, raw):
    self._raw = raw
    self.hub_name = self._parse('userData', 'hubName', converter=
        base64_to_unicode)
    self.ip = self._parse('userData', 'ip')
    self.ssid = self._parse('userData', 'ssid')