def _x_format(self):

    def date_to_str(x):
        t = seconds_to_time(x)
        return self.x_value_formatter(t)
    return date_to_str