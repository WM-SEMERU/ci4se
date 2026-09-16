def get_tile_dims(tile_dims, imshape):
    if tile_dims is None:
        td = None
    else:
        td = numpy.array(tile_dims, dtype='i8')
        nd = len(imshape)
        if td.size != nd:
            msg = 'expected tile_dims to have %d dims, got %d' % (td.size, nd)
            raise ValueError(msg)
    return td