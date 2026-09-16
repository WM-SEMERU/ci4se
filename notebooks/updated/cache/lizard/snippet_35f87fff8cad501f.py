def clicked(self, px, py):
    if self.hidden:
        return None
    if abs(px - self.posx) > self.width / 2 or abs(py - self.posy
        ) > self.height / 2:
        return None
    return math.sqrt((px - self.posx) ** 2 + (py - self.posy) ** 2)