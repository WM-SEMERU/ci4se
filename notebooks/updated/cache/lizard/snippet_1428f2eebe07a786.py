def hue_sat_to_cmap(hue, sat):
    import colorsys
    hue = float(hue) / 360.0
    sat = float(sat) / 100.0
    res = []
    for val in range(256):
        hsv_val = float(val) / 255.0
        r, g, b = colorsys.hsv_to_rgb(hue, sat, hsv_val)
        res.append((r, g, b))
    return res