def TriadicScheme(self, angle=120, mode='ryb'):
    h, s, l = self.__hsl
    angle = min(angle, 120) / 2.0
    if mode == 'ryb':
        h = Color.RgbToRyb(h)
    h += 180
    h1 = (h - angle) % 360
    h2 = (h + angle) % 360
    if mode == 'ryb':
        h1 = Color.RybToRgb(h1)
        h2 = Color.RybToRgb(h2)
    return Color((h1, s, l), 'hsl', self.__a, self.__wref), Color((h2, s, l
        ), 'hsl', self.__a, self.__wref)