def Point(pos=(0, 0, 0), r=12, c='red', alpha=1):
    if len(pos) == 2:
        pos = pos[0], pos[1], 0
    actor = Points([pos], r, c, alpha)
    return actor