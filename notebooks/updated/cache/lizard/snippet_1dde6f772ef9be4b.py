def draw(self, gdefs, theme):
    for g in gdefs:
        g.theme = theme
        g._set_defaults()
    return [g.draw() for g in gdefs]