def draw(self, ar, can, x_tick, x_label, y):
    rect_size = self.get_rect_size()
    line_len = self.get_line_len()
    nr_lines = len(self.label.split('\n'))
    text_height = font.text_height(self.label)[0]
    line_height = text_height / float(nr_lines)
    y_center = y + text_height - line_height / 1.5
    if self.fill_style != None:
        can.rectangle(self.line_style, self.fill_style, x_tick, y_center - 
            rect_size / 2.0, x_tick + rect_size, y_center + rect_size / 2.0)
    elif self.line_style != None:
        can.line(self.line_style, x_tick, y_center, x_tick + line_len, y_center
            )
        if self.tick_mark != None:
            self.tick_mark.draw(can, x_tick + line_len / 2.0, y_center)
    elif self.tick_mark != None:
        self.tick_mark.draw(can, x_tick, y_center)
    can.show(x_label, y, self.label)