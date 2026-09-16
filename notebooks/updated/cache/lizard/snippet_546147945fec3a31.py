def polygon(surf, points, color):
    gfxdraw.aapolygon(surf, points, color)
    gfxdraw.filled_polygon(surf, points, color)
    x = min([x for x, y in points])
    y = min([y for x, y in points])
    xm = max([x for x, y in points])
    ym = max([y for x, y in points])
    return pygame.Rect(x, y, xm - x, ym - y)