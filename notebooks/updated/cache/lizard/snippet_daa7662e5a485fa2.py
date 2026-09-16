def fill_rect(framebuf, x, y, width, height, color):
    while height > 0:
        index = (y >> 3) * framebuf.stride + x
        offset = y & 7
        for w_w in range(width):
            framebuf.buf[index + w_w] = framebuf.buf[index + w_w] & ~(1 <<
                offset) | (color != 0) << offset
        y += 1
        height -= 1