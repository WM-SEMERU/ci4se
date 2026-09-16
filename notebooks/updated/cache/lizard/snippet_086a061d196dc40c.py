def validate(self, value):
    try:
        if not self.blank or value:
            v = int(value)
            if v < self.imin or v > self.imax:
                return None
        return value
    except ValueError:
        return None