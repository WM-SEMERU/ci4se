def _effectinit_enlarge_font_on_focus(self, name, **kwargs):
    self._effects[name] = kwargs
    if 'font' not in kwargs:
        raise TypeError('enlarge_font_on_focus: font parameter is required')
    if 'size' not in kwargs:
        raise TypeError('enlarge_font_on_focus: size parameter is required')
    if 'enlarge_time' not in kwargs:
        kwargs['enlarge_time'] = 0.5
    if 'enlarge_factor' not in kwargs:
        kwargs['enlarge_factor'] = 2.0
    kwargs['raise_font_ps'] = kwargs['enlarge_factor'] / kwargs['enlarge_time']
    for option in self.options:
        option['font'] = pygame.font.Font(kwargs['font'], kwargs['size'])
        option['font_current_size'] = kwargs['size']
        option['raise_font_factor'] = 1.0