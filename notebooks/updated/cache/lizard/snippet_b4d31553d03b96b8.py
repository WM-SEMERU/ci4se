def new_pos(self, html_div):
    pos = self.Position(self, html_div)
    pos.bind_mov()
    self.positions.append(pos)
    return pos