def _curve(x1, y1, x2, y2, hunit=HUNIT, vunit=VUNIT):
    ax1, ax2, axm = x1 * hunit, x2 * hunit, (x1 + x2) * hunit / 2
    ay1, ay2 = y1 * vunit, y2 * vunit
    return pyx.path.curve(ax1, ay1, axm, ay1, axm, ay2, ax2, ay2)