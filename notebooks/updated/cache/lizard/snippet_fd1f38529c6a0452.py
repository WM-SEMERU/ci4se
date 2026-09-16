def prep_image(image, tile_size):
    w, h = image.size
    x_tiles = w / tile_size
    y_tiles = h / tile_size
    new_w = x_tiles * tile_size
    new_h = y_tiles * tile_size
    if new_w == w and new_h == h:
        return image
    else:
        crop_bounds = 0, 0, new_w, new_h
        return image.crop(crop_bounds)