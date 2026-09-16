def set_hex_color(self, color, *, index=0, transition_time=None):
    values = {ATTR_LIGHT_COLOR_HEX: color}
    if transition_time is not None:
        values[ATTR_TRANSITION_TIME] = transition_time
    return self.set_values(values, index=index)