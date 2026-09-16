def make_transparent(image):
    data = image.copy().getdata()
    modified = []
    for item in data:
        if _check_pixel(item) is True:
            modified.append((255, 255, 255, 255))
            continue
        modified.append(item)
    image.putdata(modified)
    return image