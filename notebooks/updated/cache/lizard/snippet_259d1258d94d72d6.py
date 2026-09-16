def _intersect(self, label, xmin, ymin, xmax, ymax):
    left = np.maximum(label[:, (0)], xmin)
    right = np.minimum(label[:, (2)], xmax)
    top = np.maximum(label[:, (1)], ymin)
    bot = np.minimum(label[:, (3)], ymax)
    invalid = np.where(np.logical_or(left >= right, top >= bot))[0]
    out = label.copy()
    out[:, (0)] = left
    out[:, (1)] = top
    out[:, (2)] = right
    out[:, (3)] = bot
    out[(invalid), :] = 0
    return out