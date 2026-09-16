def function(x, y, amp, a_x, a_y, center_x, center_y):
    x_shift = x - center_x
    y_shift = y - center_y
    A = np.pi * a_x * a_y
    dist = (x_shift / a_x) ** 2 + (y_shift / a_y) ** 2
    torus = np.zeros_like(x)
    torus[dist <= 1] = 1
    return amp / A * torus