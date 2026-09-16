def color(self, n):
    red = int(n * self.shade_factor)
    if red > 255:
        red = 255
    return red, 50, 100