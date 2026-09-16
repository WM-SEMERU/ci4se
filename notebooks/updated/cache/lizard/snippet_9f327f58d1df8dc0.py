def is_on_screen(self):
    width = self.get_width()
    height = self.get_height()
    loc = self.location()
    el_x_left = loc['x']
    el_x_right = el_x_left + width
    el_y_top = loc['y']
    el_y_bottom = el_y_top + height
    screen_size = self.driver_wrapper.get_window_size()
    screen_x = screen_size['width']
    screen_y = screen_size['height']
    if (el_x_left > 0 and el_x_right < screen_x or el_x_right > 0 and 
        el_x_right < screen_x) and (el_y_top > 0 and el_y_top < screen_y or
        el_y_bottom > 0 and el_y_bottom > screen_y):
        return True
    return False