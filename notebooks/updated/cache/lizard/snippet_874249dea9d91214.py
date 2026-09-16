def scale_pixels(color, layer):
    pixelmap = []
    for pix_x in range(MAX_X + 1):
        for pix_y in range(MAX_Y + 1):
            y1 = pix_y * dotsize[0]
            x1 = pix_x * dotsize[1]
            y2 = pix_y * dotsize[0] + (dotsize[0] - 1)
            x2 = pix_x * dotsize[1] + (dotsize[1] - 1)
            if y1 <= MAX_Y and y2 <= MAX_Y:
                if x1 <= MAX_X and x2 <= MAX_X:
                    if (pix_x, pix_y) in layer:
                        pixelmap.append([(y1, x1), (y2, x2), color])
    return pixelmap