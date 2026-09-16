def set_border_style_type(self, border_style_type):
    style = self.__border_style_factory.create_border(border_style_type)
    self.set_border_style(style)
    return self