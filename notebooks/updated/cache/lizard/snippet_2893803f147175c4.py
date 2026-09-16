def font(self, container):
    typeface = self.get_style('typeface', container)
    weight = self.get_style('font_weight', container)
    slant = self.get_style('font_slant', container)
    width = self.get_style('font_width', container)
    return typeface.get_font(weight=weight, slant=slant, width=width)