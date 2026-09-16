def ColorWithLightness(self, lightness):
    h, s, l = self.__hsl
    return Color((h, s, lightness), 'hsl', self.__a, self.__wref)