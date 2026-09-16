def _edge_data_to_sframe(data, src_field, dst_field):
    if isinstance(data, SFrame):
        if (src_field is None and dst_field is None and _SRC_VID_COLUMN in
            data.column_names() and _DST_VID_COLUMN in data.column_names()):
            return data
        if src_field is None:
            raise ValueError('src_field must be specified for SFrame input')
        if dst_field is None:
            raise ValueError('dst_field must be specified for SFrame input')
        data_copy = copy.copy(data)
        if src_field == _DST_VID_COLUMN and dst_field == _SRC_VID_COLUMN:
            dst_id_column = data_copy[_DST_VID_COLUMN]
            del data_copy[_DST_VID_COLUMN]
            data_copy.rename({_SRC_VID_COLUMN: _DST_VID_COLUMN}, inplace=True)
            data_copy[_SRC_VID_COLUMN] = dst_id_column
        else:
            data_copy.rename({src_field: _SRC_VID_COLUMN, dst_field:
                _DST_VID_COLUMN}, inplace=True)
        return data_copy
    elif HAS_PANDAS and type(data) == pd.DataFrame:
        if src_field is None:
            raise ValueError('src_field must be specified for Pandas input')
        if dst_field is None:
            raise ValueError('dst_field must be specified for Pandas input')
        sf = SFrame(data)
        if src_field == _DST_VID_COLUMN and dst_field == _SRC_VID_COLUMN:
            dst_id_column = data_copy[_DST_VID_COLUMN]
            del sf[_DST_VID_COLUMN]
            sf.rename({_SRC_VID_COLUMN: _DST_VID_COLUMN}, inplace=True)
            sf[_SRC_VID_COLUMN] = dst_id_column
        else:
            sf.rename({src_field: _SRC_VID_COLUMN, dst_field:
                _DST_VID_COLUMN}, inplace=True)
        return sf
    elif type(data) == Edge:
        return _edge_list_to_sframe([data], _SRC_VID_COLUMN, _DST_VID_COLUMN)
    elif type(data) == list:
        return _edge_list_to_sframe(data, _SRC_VID_COLUMN, _DST_VID_COLUMN)
    else:
        raise TypeError('Edges type %s is Not supported.' % str(type(data)))