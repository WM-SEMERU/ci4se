def table_to_source_list(table, src_type=OutputSource):
    source_list = []
    if table is None:
        return source_list
    for row in table:
        src = src_type()
        for param in src_type.names:
            if param in table.colnames:
                val = row[param]
                if isinstance(val, np.float32):
                    val = np.float64(val)
                setattr(src, param, val)
        source_list.append(src)
    return source_list