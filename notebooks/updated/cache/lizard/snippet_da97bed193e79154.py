def add_mountains(self):
    from noise import pnoise2
    import random
    random.seed()
    octaves = random.random() * 0.5 + 0.5
    freq = 17.0 * octaves
    for y in range(self.grd.grid_height - 1):
        for x in range(self.grd.grid_width - 1):
            pixel = self.grd.get_tile(y, x)
            if pixel == 'X':
                n = int(pnoise2(x / freq, y / freq, 1) * 11 + 5)
                if n < 1:
                    self.grd.set_tile(y, x, '#')