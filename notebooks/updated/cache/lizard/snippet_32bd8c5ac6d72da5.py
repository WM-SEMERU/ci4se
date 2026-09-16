def set_pwm(self, led_num, value):
    self.__check_range('led_number', led_num)
    self.__check_range('led_value', value)
    register_low = self.calc_led_register(led_num)
    self.write(register_low, value_low(value))
    self.write(register_low + 1, value_high(value))