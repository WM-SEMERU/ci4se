def is_visible(self, x, y):
    return (x >= 0 and x <= self.width and y >= self._start_line and y < 
        self._start_line + self.height)