def apparent_dip_correction(axes):
    a1 = axes[0].copy()
    a1[-1] = 0
    cosa = angle(axes[0], a1, cos=True)
    _ = 1 - cosa ** 2
    if _ > 1e-12:
        sina = N.sqrt(_)
        if cosa < 0:
            sina *= -1
        R = N.array([[cosa, sina], [-sina, cosa]])
    else:
        R = N.identity(2)
    return R