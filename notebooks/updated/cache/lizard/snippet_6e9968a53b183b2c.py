def generate_scan_parameter_description(scan_parameters):
    table_description = np.dtype([(key, tb.Int32Col(pos=idx)) for idx, key in
        enumerate(scan_parameters)])
    return table_description