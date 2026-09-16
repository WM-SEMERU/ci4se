def triangulize(image, tile_size):
    if isinstance(image, basestring) or hasattr(image, 'read'):
        image = Image.open(image)
    assert isinstance(tile_size, int)
    if tile_size == 0:
        tile_size = guess_tile_size(image)
    if tile_size % 2 != 0:
        tile_size = tile_size / 2 * 2
    logging.info('Input image size: %r', image.size)
    logging.info('Tile size: %r', tile_size)
    image = prep_image(image, tile_size)
    logging.info('Prepped image size: %r', image.size)
    pix = image.load()
    draw = ImageDraw.Draw(image)
    for x, y in iter_tiles(image, tile_size):
        process_tile(x, y, tile_size, pix, draw, image)
    return image