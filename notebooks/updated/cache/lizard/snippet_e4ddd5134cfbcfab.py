def triangle_colors(tile_x, tile_y, tile_size, pix):
    quad_size = tile_size / 2
    north = []
    for y in xrange(tile_y, tile_y + quad_size):
        x_off = y - tile_y
        for x in xrange(tile_x + x_off, tile_x + tile_size - x_off):
            north.append(pix[x, y])
    south = []
    for y in xrange(tile_y + quad_size, tile_y + tile_size):
        x_off = tile_y + tile_size - y
        for x in xrange(tile_x + x_off, tile_x + tile_size - x_off):
            south.append(pix[x, y])
    east = []
    for x in xrange(tile_x, tile_x + quad_size):
        y_off = x - tile_x
        for y in xrange(tile_y + y_off, tile_y + tile_size - y_off):
            east.append(pix[x, y])
    west = []
    for x in xrange(tile_x + quad_size, tile_x + tile_size):
        y_off = tile_x + tile_size - x
        for y in xrange(tile_y + y_off, tile_y + tile_size - y_off):
            west.append(pix[x, y])
    return map(get_average_color, [north, east, south, west])