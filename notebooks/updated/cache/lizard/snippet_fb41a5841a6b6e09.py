def move_to(self, x, y, h):
    if self._has_border:
        start_x = 1
        width = self.canvas.width - 2
        start_y = self.canvas.start_line + 1
        height = self.canvas.height - 2
    else:
        start_x = 0
        width = self.canvas.width
        start_y = self.canvas.start_line
        height = self.canvas.height
    if (x >= start_x and x < start_x + width and y >= start_y and y + h < 
        start_y + height):
        return
    if y < start_y:
        self.canvas.scroll_to(y - 1 if self._has_border else y)
    else:
        line = y + h - self.canvas.height + (1 if self._has_border else 0)
        self.canvas.scroll_to(max(0, line))