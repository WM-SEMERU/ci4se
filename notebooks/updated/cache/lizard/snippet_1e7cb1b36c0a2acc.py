def element_screen_center(self, element):
    pos = self.element_screen_position(element)
    size = element.size
    pos['top'] += int(size['height'] / 2)
    pos['left'] += int(size['width'] / 2)
    return pos