def get_led_register_from_name(self, name):
    res = re.match('^led_([0-9]{1,2})$', name)
    if res is None:
        raise AttributeError("Unknown attribute: '%s'" % name)
    led_num = int(res.group(1))
    if led_num < 0 or led_num > 15:
        raise AttributeError("Unknown attribute: '%s'" % name)
    return self.calc_led_register(led_num)