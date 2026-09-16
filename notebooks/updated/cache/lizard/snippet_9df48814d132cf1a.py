def _get_field(xdmf_file, data_item):
    shp = _get_dim(data_item)
    h5file, group = data_item.text.strip().split(':/', 1)
    icore = int(group.split('_')[-2]) - 1
    fld = _read_group_h5(xdmf_file.parent / h5file, group).reshape(shp)
    return icore, fld