def set_rgb_color(self, red, green, blue, effect=EFFECT_SUDDEN,
    transition_time=MIN_TRANSITION_TIME):
    if self.is_off():
        raise Exception(
            "set_rgb_color can't be used if the bulb is off. Turn it on first")
    schema = Schema({'red': All(int, Range(min=0, max=255)), 'green': All(
        int, Range(min=0, max=255)), 'blue': All(int, Range(min=0, max=255)
        ), 'effect': Any(self.EFFECT_SUDDEN, self.EFFECT_SMOOTH),
        'transition_time': All(int, Range(min=30))})
    schema({'red': red, 'green': green, 'blue': blue, 'effect': effect,
        'transition_time': transition_time})
    rgb = red * 65536 + green * 256 + blue
    params = [rgb, effect, transition_time]
    self.api_call.operate_on_bulb('set_rgb', params)
    self.property[self.PROPERTY_NAME_RGB_COLOR] = rgb