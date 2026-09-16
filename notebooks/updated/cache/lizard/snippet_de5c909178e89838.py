def iget_list_column_slice(list_, start=None, stop=None, stride=None):
    if isinstance(start, slice):
        slice_ = start
    else:
        slice_ = slice(start, stop, stride)
    return (row[slice_] for row in list_)