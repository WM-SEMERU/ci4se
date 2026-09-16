def parse_number(self):
    value = self.current_token.value
    suffix = value[-1].lower()
    try:
        if suffix in NUMBER_SUFFIXES:
            return NUMBER_SUFFIXES[suffix](value[:-1])
        return Double(value) if '.' in value else Int(value)
    except (OutOfRange, ValueError):
        return String(value)