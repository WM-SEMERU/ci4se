def set_led_brightness(self, brightness):
    set_cmd = self._create_set_property_msg('_led_brightness', 7, brightness)
    self._send_method(set_cmd, self._property_set)