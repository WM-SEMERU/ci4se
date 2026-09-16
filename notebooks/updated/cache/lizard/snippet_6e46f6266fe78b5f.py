def set_leds(self, hue: float=0.0, saturation: float=1.0, value: float=1.0):
    r, g, b = hsv_to_rgb(hue, saturation, value)
    write_led_value(self.device_unique_name, 'red', r * 255.0)
    write_led_value(self.device_unique_name, 'green', g * 255.0)
    write_led_value(self.device_unique_name, 'blue', b * 255.0)