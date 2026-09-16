def fromhdf5sorted(source, where=None, name=None, sortby=None, checkCSI=
    False, start=None, stop=None, step=None):
    assert sortby is not None, 'no column specified to sort by'
    return HDF5SortedView(source, where=where, name=name, sortby=sortby,
        checkCSI=checkCSI, start=start, stop=stop, step=step)