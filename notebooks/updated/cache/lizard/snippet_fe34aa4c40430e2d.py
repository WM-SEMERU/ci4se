def strel_line(length, angle):
    angle = float(angle) * np.pi / 180.0
    x_off = int(np.finfo(float).eps + np.cos(angle) * length / 2)
    y_off = -int(np.finfo(float).eps + np.sin(angle) * length / 2)
    x_center = abs(x_off)
    y_center = abs(y_off)
    strel = np.zeros((y_center * 2 + 1, x_center * 2 + 1), bool)
    draw_line(strel, (y_center - y_off, x_center - x_off), (y_center,
        x_center), True)
    draw_line(strel, (y_center + y_off, x_center + x_off), (y_center,
        x_center), True)
    return strel