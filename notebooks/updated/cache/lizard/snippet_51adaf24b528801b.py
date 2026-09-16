def pygame_image_loader(filename, colorkey, **kwargs):
    if colorkey:
        colorkey = pygame.Color('#{0}'.format(colorkey))
    pixelalpha = kwargs.get('pixelalpha', True)
    image = pygame.image.load(filename)

    def load_image(rect=None, flags=None):
        if rect:
            try:
                tile = image.subsurface(rect)
            except ValueError:
                logger.error('Tile bounds outside bounds of tileset image')
                raise
        else:
            tile = image.copy()
        if flags:
            tile = handle_transformation(tile, flags)
        tile = smart_convert(tile, colorkey, pixelalpha)
        return tile
    return load_image