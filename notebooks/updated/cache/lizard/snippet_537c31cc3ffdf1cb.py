def Text(text, font, color=pygame.Color(0, 0, 0), antialias=False, align=
    'center'):
    assert align in ['center', 'left', 'right']
    margin_l, margin_r = 1, 1
    if align == 'left':
        margin_l = 0
    elif align == 'right':
        margin_r = 0
    margin = Margin(margin_l, margin_r)
    color_key = pygame.Color(0, 0, 1) if pygame.Color(0, 0, 1) != color else 2
    text_surfaces = _lmap(lambda text: _text(text, font=font, color=color,
        antialias=antialias), map(methodcaller('strip'), text.split('\n')))
    w = max(surf.get_rect().w for surf in text_surfaces)
    h = sum(surf.get_rect().h for surf in text_surfaces)
    surf = compose((w, h), Fill(color_key))(LinLayout('v')(*_lmap(lambda s:
        Surface(margin)(s), text_surfaces)))
    surf.set_colorkey(color_key)
    return surf.convert_alpha()