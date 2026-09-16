def longest_dimension_first(vector, start=(0, 0), width=None, height=None):
    x, y = start
    out = []
    for dimension, magnitude in sorted(enumerate(vector), key=lambda x: abs
        (x[1]) + random.random(), reverse=True):
        if magnitude == 0:
            break
        sign = 1 if magnitude > 0 else -1
        for _ in range(abs(magnitude)):
            if dimension == 0:
                dx, dy = sign, 0
            elif dimension == 1:
                dx, dy = 0, sign
            elif dimension == 2:
                dx, dy = -sign, -sign
            x += dx
            y += dy
            if width is not None:
                x %= width
            if height is not None:
                y %= height
            direction = Links.from_vector((dx, dy))
            out.append((direction, (x, y)))
    return out