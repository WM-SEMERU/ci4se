def get(self, start=None, count=None, stride=None):
    try:
        sds_name, rank, dim_sizes, data_type, n_attrs = self.info()
        if isinstance(dim_sizes, type(1)):
            dim_sizes = [dim_sizes]
    except HDF4Error:
        raise HDF4Error('get : cannot execute')
    if start is None:
        start = [0] * rank
    elif isinstance(start, type(1)):
        start = [start]
    if count is None:
        count = dim_sizes
        if count[0] == 0:
            count[0] = 1
    elif isinstance(count, type(1)):
        count = [count]
    if stride is None:
        stride = [1] * rank
    elif isinstance(stride, type(1)):
        stride = [stride]
    if len(start) != rank or len(count) != rank or len(stride) != rank:
        raise HDF4Error('get : start, stride or count do not match SDS rank')
    for n in range(rank):
        if start[n] < 0 or start[n] + (abs(count[n]) - 1) * stride[n
            ] >= dim_sizes[n]:
            raise HDF4Error(
                'get arguments violate the size (%d) of dimension %d' % (
                dim_sizes[n], n))
    if not data_type in SDC.equivNumericTypes:
        raise HDF4Error('get cannot currrently deal with the SDS data type')
    return _C._SDreaddata_0(self._id, data_type, start, count, stride)