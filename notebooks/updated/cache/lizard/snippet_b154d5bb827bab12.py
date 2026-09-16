def adjustColors(self, mode='dark'):
    rp = Game.__color_modes.get(mode, {})
    for k, color in self.__colors.items():
        self.__colors[k] = rp.get(color, color)