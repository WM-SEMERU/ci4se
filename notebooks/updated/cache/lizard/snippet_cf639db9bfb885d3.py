def parse_object(self, data):
    for key, value in data.items():
        if isinstance(value, (str, type(''))) and self.strict_iso_match.match(
            value):
            data[key] = dateutil.parser.parse(value)
    return data