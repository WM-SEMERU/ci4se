def _write_imgdata(img, data, tr, x=0, y=0):
    for pixel, (x1, y1) in zip(data, tr):
        img.putpixel((x + x1, y + y1), pixel)
    return img