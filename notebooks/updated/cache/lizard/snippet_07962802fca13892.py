def make_spiral_texture(spirals=6.0, ccw=False, offset=0.0, resolution=1000):
    dist = np.sqrt(np.linspace(0.0, 1.0, resolution))
    if ccw:
        direction = 1.0
    else:
        direction = -1.0
    angle = dist * spirals * np.pi * 2.0 * direction
    spiral_texture = np.cos(angle) * dist / 2.0 + 0.5, np.sin(angle
        ) * dist / 2.0 + 0.5
    return spiral_texture