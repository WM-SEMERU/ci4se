def rmBorder(img, border=None):
    if border is None:
        pass
    elif len(border) == 2:
        s0 = slice(border[0][1], border[1][1])
        s1 = slice(border[0][0], border[1][0])
        img = img[s0, s1]
    elif len(border) == 4:
        x = np.unique(border[:, (0)])
        y = np.unique(border[:, (1)])
        if len(x) == 2 and len(y) == 2:
            s0 = slice(y[0], y[1])
            s1 = slice(x[0], x[1])
            img = img[s0, s1]
        else:
            img = simplePerspectiveTransform(img, border)
    else:
        raise Exception('[border] input wrong')
    return img