def center(self, max_width):
    old_width, height = self._im.size
    new_size = max_width, height
    new_im = Image.new('1', new_size)
    paste_x = int((max_width - old_width) / 2)
    new_im.paste(self._im, (paste_x, 0))
    self._im = new_im