def check_overscan(xstart, xsize, total_prescan_pixels=24,
    total_science_pixels=4096):
    hasoverscan = False
    leading = 0
    trailing = 0
    if xstart < total_prescan_pixels:
        hasoverscan = True
        leading = abs(xstart - total_prescan_pixels)
    if xstart + xsize > total_science_pixels:
        hasoverscan = True
        trailing = abs(total_science_pixels - (xstart + xsize -
            total_prescan_pixels))
    return hasoverscan, leading, trailing