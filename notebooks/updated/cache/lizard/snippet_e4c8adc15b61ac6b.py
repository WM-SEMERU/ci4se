def rectangle(bounds, **kwargs):
    from .path import Path2D
    bounds = np.asanyarray(bounds, dtype=np.float64)
    if bounds.shape == (2,):
        half = np.abs(bounds) / 2.0
        bounds = np.array([-half, half])
    if not (util.is_shape(bounds, (2, 2)) or util.is_shape(bounds, (-1, 2, 2))
        ):
        raise ValueError('bounds must be (m, 2, 2) or (2, 2)')
    lines = []
    vertices = []
    for lower, upper in bounds.reshape((-1, 2, 2)):
        lines.append(entities.Line(np.arange(5) % 4 + len(vertices)))
        vertices.extend([lower, [upper[0], lower[1]], upper, [lower[0],
            upper[1]]])
    rect = Path2D(entities=lines, vertices=vertices, **kwargs)
    return rect