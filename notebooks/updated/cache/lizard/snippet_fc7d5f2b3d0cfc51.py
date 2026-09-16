def _write(self, text, x, y, colour=Screen.COLOUR_WHITE, attr=Screen.
    A_NORMAL, bg=Screen.COLOUR_BLACK):
    if y >= self._height or x >= self._width:
        return
    if len(text) + x > self._width:
        text = text[:self._width - x]
    self._plain_image[y] = text.join([self._plain_image[y][:x], self.
        _plain_image[y][x + len(text):]])
    for i, _ in enumerate(text):
        self._colour_map[y][x + i] = colour, attr, bg