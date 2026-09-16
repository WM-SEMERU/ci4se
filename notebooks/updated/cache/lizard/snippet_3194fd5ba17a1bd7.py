def block_transfer(self, buffer, x, y):
    block_min_x = max(0, x)
    block_max_x = min(x + buffer.width, self._width)
    if block_min_x > block_max_x:
        return
    for by in range(0, self._height):
        if y <= by < y + buffer.height:
            self._double_buffer[by][block_min_x:block_max_x] = buffer.slice(
                block_min_x - x, by - y, block_max_x - block_min_x)