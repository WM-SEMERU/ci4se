def _get_oshape_of_gather_nd_op(dshape, ishape):
    assert len(dshape) > 0 and len(ishape) > 0
    oshape = list(ishape[1:])
    if ishape[0] < len(dshape):
        oshape.extend(dshape[ishape[0]:])
    return tuple(oshape)