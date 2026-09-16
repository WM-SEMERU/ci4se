def has_color(self):
    if self.get_value(CONST.STATUSES_KEY).get('color_mode') == str(CONST.
        COLOR_MODE_ON):
        return True
    return False