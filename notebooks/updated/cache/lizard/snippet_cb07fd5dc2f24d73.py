def _parse_led(self, keypad, component_xml):
    component_num = int(component_xml.get('ComponentNumber'))
    led_num = component_num - 80
    led = Led(self._lutron, keypad, name='LED %d' % led_num, led_num=
        led_num, component_num=component_num)
    return led