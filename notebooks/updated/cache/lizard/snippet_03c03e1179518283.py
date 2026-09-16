def parse_option(self, option, block_name, *values):
    try:
        if len(values) != 1:
            raise TypeError
        self.total_duration = int(values[0])
        if self.total_duration <= 0:
            raise ValueError
    except ValueError:
        pattern = '"{0}" must be an integer > 0'
        raise ValueError(pattern.format(option))