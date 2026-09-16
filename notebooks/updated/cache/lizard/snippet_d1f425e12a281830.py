def validate(self, value):
    try:
        if not self.blank or value:
            v = int(value)
            if v < 0:
                return None
        return value
    except ValueError:
        return None