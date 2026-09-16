def set_border_style(self, border_style):
    if not isinstance(border_style, MenuBorderStyle):
        raise TypeError('border_style must be type MenuBorderStyle')
    self.__header.style.border_style = border_style
    self.__prologue.style.border_style = border_style
    self.__items_section.style.border_style = border_style
    self.__epilogue.style.border_style = border_style
    self.__footer.style.border_style = border_style
    self.__prompt.style.border_style = border_style
    return self